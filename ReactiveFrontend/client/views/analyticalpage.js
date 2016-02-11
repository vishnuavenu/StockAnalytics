/**
 * Created by vishnu on 11/2/16.
 */
Template.landingPage.events({
    'click .to_analytic': function(event){
        event.preventDefault();
        Router.go("stockhome");
    },

    'click .to_portfolio': function(event){
        event.preventDefault();
        Router.go("portfolio");
    }
});

Template.analyticPage.helpers({

});