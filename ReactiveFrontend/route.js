
///////////////////////////////////
//Defining Routes////////////////
/////////////////////////////////

//Route configuration
Router.configure({
  layoutTemplate: "main"
});

Router.route("/", {
  name: "landing",
  template: "landingPage"
});

Router.route("/stocks",{
  name: "stockhome",
  template:"analyticPage"
});

Router.route("/portfolio",{
  name: "portfolio",
  template: "portfolioPage"
});