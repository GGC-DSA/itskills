// ************** Generate the tree diagram  *****************
var width = window.innerWidth; // Use the window's width
var height = window.innerHeight; // Use the window's height

var i = 0,
  duration = 750,
  root;

var tree = d3.layout.tree().size([height, width]);

var diagonal = d3.svg.diagonal().projection(function (d) {
  return [d.x, d.y];
});

var svg = d3
  .select("body")
  .append("svg")
  .attr("viewBox", "-160 -50 1300 700")
  .classed("svg-content-responsive", true);

svg
  .append("rect")
  .attr("width", "75%")
  .attr("height", "100%")
  .attr("fill", "#d7e1ec")
  .attr("rx", "10%");

var aspect = width / height,
  chart = d3.select("#chart");
d3.select(window).on("resize", function () {
  var targetWidth = chart.node().getBoundingClientRect().width;
  chart.attr("width", targetWidth);
  chart.attr("height", targetWidth / aspect);
});

root = treeJson[0];
root.x0 = height / 2;
root.y0 = 0;

update(root);

d3.select(self.frameElement).style("height", "500px");

function update(source) {
  // Compute the new tree layout.
  var nodes = tree.nodes(root).reverse(),
    links = tree.links(nodes);

  // Normalize for fixed-depth y.
  nodes.forEach(function (d) {
    d.y = d.depth * 180; // Modified to increase horizontal spacing between nodes
  });

  // Update the nodes…
  var node = svg.selectAll("g.node").data(nodes, function (d) {
    return d.id || (d.id = ++i);
  });

  // Enter any new nodes at the parent's previous position. added
  var nodeEnter = node
    .enter()
    .append("g")
    .attr("class", "node")
    .attr("transform", function (d) {
      return "translate(" + source.y0 + "," + source.x0 + ")"; // Modified to start from left center
    })
    .on("click", click);

  nodeEnter
    .append("circle")
    .attr("r", function (d) {
      return d.value;
    })
    .style("stroke", function (d) {
      return d.type;
    })
    .style("fill", function (d) {
      return d.level;
    })
    // adds hover effect
    .attr("r", 4.5)
    .on("mouseover", function (d) {
      d3.select(this.parentNode).select("text").style("fill", "blue");
    })
    .on("mouseout", function (d) {
      d3.select(this.parentNode).select("text").style("fill", "black");
    });

  nodeEnter
    .append("text")
    .attr("y", function (d) {
      return d.children || d._children ? -18 : 18;
    })
    .attr("dy", "0em")
    .attr("text-anchor", "middle")
    .text(function (d) {
      if (d.classNum == null) {
        return d.name;
      } else {
        return d.name;
      }
    })
    .style("fill-opacity", 1);

  // Transition nodes to their new position.
  var nodeUpdate = node
    .transition()
    .duration(duration)
    .attr("transform", function (d) {
      // Adjust the source.y coordinate of the first node (root node)
      if (d === root) {
        return "translate(" + d.y + "," + (d.x - 150) + ")";
      }
      return "translate(" + d.y + "," + d.x + ")";
    });

  nodeUpdate
    .select("circle")
    .attr("r", function (d) {
      return d.value;
    })
    .style("stroke", function (d) {
      return d.type;
    })
    .style("fill", function (d) {
      return d.level;
    });

  nodeUpdate.select("text").style("fill-opacity", 1);

  // Transition exiting nodes to the parent's new position.
  var nodeExit = node
    .exit()
    .transition()
    .duration(duration)
    .attr("transform", function (d) {
      return "translate(" + source.y + "," + source.x + ")";
    })
    .remove();

  nodeExit.select("circle").attr("r", 1e-6);

  nodeExit.select("text").style("fill-opacity", 1e-6);

  // Update the links…
  var link = svg.selectAll("path.link").data(links, function (d) {
    return d.target.id;
  });

  // Enter the links.
  link
    .enter()
    .insert("path", "g")
    .attr("class", "link")
    .style("stroke", function (d) {
      return d.target.level;
    })
    .attr("d", diagonal);

  // Transition links to their new position.
  link.transition().duration(duration).attr("d", diagonal);

  // Transition exiting nodes to the parent's new position.
  link
    .exit()
    .transition()
    .duration(duration)
    .attr("d", function (d) {
      var o = { y: source.y, x: source.x };
      return diagonal({ source: o, target: o });
    })
    .remove();

  // Stash the old positions for transition.
  nodes.forEach(function (d) {
    d.y0 = d.y;
    d.x0 = d.x;
  });
}

// Toggle children on click.
function click(d) {
  if (d.children) {
    d._children = d.children;
    d.children = null;
  } else {
    d.children = d._children;
    d._children = null;
  }
  update(d);
}
