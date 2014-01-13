var RatingStars;

RatingStars = (function() {

  function RatingStars($el, options) {
    this.el = $el;
    this.options = options;
    this.buildUI();
  }

  RatingStars.prototype.buildUI = function() {
    var thanks, _self;
    _self = this;
    thanks = function(score) {
      return feedBack.add("Thanks for rating!<br /> You rated this " + score + " stars.", "feedback", 2500);
    };
    return this.el.raty({
      path: "/static/js/jqplugins/raty/img/",
      start: this.options.rating,
      half: true,
      width: 150,
      readOnly: this.options.readonly,
      size: 24,
      starHalf: "star-half-big.png",
      starOff: "star-off-big.png",
      starOn: "star-on-big.png",
      click: function(score, evt) {
        var params;
        params = {
          entryId: _self.options.id,
          categoryString: _self.options.category,
          ratingParam: score * 2
        };
        return ___saveJQFromPrototype.ajax({
          url: '/edit/rate',
          data: params,
          type: "POST",
          success: function(response) {
            if (typeof feedBack === "undefined") {
              head.js("/static/js/feedback.jq.js");
              return head.ready(function() {
                return thanks(_self.el.raty("score"));
              });
            } else {
              return thanks(_self.el.raty("score"));
            }
          }
        });
      }
    });
  };

  return RatingStars;

})();
