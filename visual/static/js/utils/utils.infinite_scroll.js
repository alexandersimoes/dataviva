function infinite_scroll(selection){
  var url = window.location.href;
  
  // Initialize variables
  var formatDate = d3.time.format("%B %-d, %Y"),
      parseDate = d3.time.format.iso.parse,
      offset = 0,
      fetching;
  
  scroll = function(selection) {
    selection.each(function(data_passed) {
      var container_el = this;
      
      // On first time add
      d3.select(container_el).selectAll(".loading")
        .data([container_el])
        .enter().append("div")
        .attr("class", "loading")
      
      // The item we're going to listen on for scrolling
      d3.select(window)
          .on("scroll", maybe_fetch)
      
      // Check if we need to fetch
      function maybe_fetch() {

        // get the position of the loading div
        var loading_div_y = !d3.select(".loading").empty() ? d3.select(".loading").node().getBoundingClientRect().top : NaN;

        // if we're not currently fetching and offset if not NaN and the loader
        // y pos is less than the height of the page then fetch new items
        if (!fetching && offset >= 0 && loading_div_y < innerHeight) {
          fetch();
        }

      }
      
      // Call the server for more acitivities
      function fetch() {
        fetching = true;
  
        // Here we set the header X-Requested-With to XMLHttpRequest so the 
        // server knows it's an AJAX call
        d3.json(url+"?offset="+offset)
          .header("X-Requested-With", "XMLHttpRequest")
          .get(display);
      }
      
      // The meat and potatoes, this function get called after we've made the 
      // call to the server
      function display(error, new_data) {
        
        // clean up data into one nice array of activities
        activities = new_data.activities.map(function(d){
          return_obj = d[1]
          return_obj["activity_type"] = d[0]
          return_obj["title"] = d[1].app_name ? d[1].app_name : d[1].question ? d[1].question : d[1].body;
          return_obj["timestamp"] = parseDate(d[1].timestamp);
          return return_obj
        });
  
        // we're obviously no longer fetching
        fetching = false;
  
        // if the server returned an empty list, return and get rid of loading
        // div
        if (!activities.length) {
          if(offset == 0){
            d3.select(container_el)
              .append("p")
              .text("No activity yet!")
          }
          offset = NaN;
          d3.select(".loading").remove();
          return;
        }
  
        // increment offset by number of items received from server
        offset += activities.length;
  
        // using d3's helpful enter/update/exit paradigm add new items from
        // the server
        var activities_enter = d3.select(container_el).selectAll(".activity")
          .data(activities, function(d){ return d.app_id })
          .enter().insert("a", "div.loading")
            .attr("class", "activity")
            .attr("href", function(d){
              var url = "#"
              if(d.activity_type == "starred"){
                url = "/embed/" + d.app_id;
              }
              else if(d.activity_type == "questions"){
                url = "/ask/question/" + d.slug;
              }
              else if(d.activity_type == "replies"){
                url = "/ask/question/" + d.question_id;
              }
              return url;
            })
            .append("div")
            .attr("class", "feed-item")
  
        // the title div housing the icon and title
        var title_div = activities_enter.append("div")
            .attr("class", "feed_title")
  
        // add icon
        title_div.append("img")
            .attr("src", function(d){
              var img_url = "/static/img/icons/tiles/";
        
              // if this is a starred app, we need to figure out which app it is
              // and use this app's icon
              if(d.activity_type == "starred"){
                var app_type = d.app_id.split("/")[0]
                img_url += app_type+"_tile.png";
              }
        
              // otherwise it's an ask sabrina question/reply
              else {
                if(d.activity_type == "questions"){
                  img_url += "question_tile.png";
                }
                else {
                  img_url += "reply_tile.png";
                }
              }
              return img_url
            })
            .attr("width", "23px")
            .attr("padding-bottom", "23px")
  
        // the title (strip out HTML!)
        title_div.append("p")
          .html(function(d){
            return d.title.replace(/(<([^>]+)>)/ig,"");
          })
  
        // lastly, the div that holds the data
        activities_enter.append("div")
            .attr("class", "feed_date")
            .text(function(d) { return formatDate(d.timestamp); });
  
        // maybe the user has a super dooper tall screen (or high resolution)
        // so we need to check if we're already at the bottem, even though we
        // just added new items
        setTimeout(maybe_fetch, 50);
        
      }
      
      // call this on page load
      maybe_fetch();
      
    })
  }
  
  scroll.url = function(value) {
    if(!arguments.length) return url;
    url = value;
    return scroll;
  }
  
  return scroll
  
}
