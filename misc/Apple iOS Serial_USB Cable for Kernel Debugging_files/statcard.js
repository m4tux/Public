function StatCard(){

    this.memberstats = $(".memberstats");

    this.red = "#ee282e";
    this.green = "#077634";
    this.blue = "#1f8bc9";
    this.orange = "#ff7b00";
    this.grey = "#ccc";

    this.calculatedColor = this.blue;
    this.colorInstructablesCounter();
    this.countHover();

}
StatCard.prototype.colorInstructablesCounter = function(){
    var obj = this;
    this.memberstats.each(function(i, el){
	var instructablesCount = parseInt($(el).children(".count")[0].innerHTML);
	if (instructablesCount > 24){
	    obj.calculatedColor = obj.orange;
	} else if (instructablesCount >= 16) {
	    obj.calculatedColor = obj.red;
	} else if (instructablesCount >= 8) {
	    obj.calculatedColor = obj.green;
	} else if (instructablesCount == 0) {
	    obj.calculatedColor = obj.grey;
	} else {
	    obj.calculatedColor = obj.blue;
	}
	$(el).css("background-color", obj.calculatedColor);
    });
}
StatCard.prototype.countHover = function(){
    var obj = this;
    this.memberstats.each(function(i, el){
        var thisCount = parseInt($(el).find('.count').html());
        if (thisCount > 0) {
            $(el).hover(function(event){
                $(el).parent().append('<div id="statcard-container" class="statcard-container"></div>');
                var target = $($(".statcard-container")[0]);
                target.attr({"style": "margin-left: 48px; *left: 5px; margin-top: -15px; margin-bottom: 15px;"});
                var authorUrl = $(el).attr('class');
                var authorname = encodeURIComponent(authorUrl.substring(authorUrl.indexOf("id-") + 3, authorUrl.length));
                var url = "/member/statscard/?screenName=" + authorname;
                target.load(url, function(data){
                    var statscard = $(target).find('.statscard')[0];
                    var cardOffset = $(statscard).offset().top;
                    var cardHeight = $(statscard).height();
                    var viewportHeight = $(window).height();
                    var offsetTop = $(window).scrollTop();
                    var cardBottom = cardOffset + cardHeight;
                    var windowBottom = viewportHeight + offsetTop;
                    if (cardBottom > windowBottom){
                    target.css("margin-top", '-' + ((cardBottom - windowBottom) + 40) + 'px');
                    }
                });
            },
            function(event){
                $('.statcard-container').remove();
            });
        }
    });
}
statCard = new StatCard();