function ___loadFeedback(cb) {
  if(typeof feedBack === "undefined") {
      head.js("/static/js/feedback.jq.js");
      head.ready(cb());
  }
  else
      cb();
}

function subscribe(type, subscriptionId, button, successcallback ) {

  // assume we're subscribing someone, unless we're told to unsubscribe them:
  var action = 'ADD';

  var el = $(button);
  if (el.hasClass('subscribeState')) {/*action is already add by default*/;}
  if (el.hasClass('unsubscribeState')) {action = "REMOVE"}

  if (el.is('input')) {
      // the old way of doing this needs an input to be modified here instead of using the callback
      // this method was abandoned because the new buttons needed icons and fancy changes; those behaviors are
      // moved to the page on which the buttons appear.
      el.val("following");
      el.attr("disabled", "true");
      el.addClass("disabled");
      el.fadeIn(100);
      el.click(function(){return false;});
  }

  $.ajax('/you/subscriptions/',{
      type: 'POST',
      data: {
          subscriptionId: subscriptionId,
          type : type,
          posted: new Date().getTime(),
          action: action
      },
      success: successcallback,
      error: function( jqXHR ) {
          ___loadFeedback(function() {feedBack.addFromJSON( jqXHR.responseText );});
      }
  });
}

function addToGuide( guideId, instructableId ) {
  $.ajax( '/edit/guideAdd', {
      type: 'POST',
      data : {
          guideId: guideId,
          instructableId: instructableId,
          posted: new Date().getTime()
      },
      success: function( data ) {
          ___loadFeedback(function() {feedBack.add(data);});
      },
      error: function( jqXHR, statusText, errorThrown ) {
          ___loadFeedback(function() {feedBack.add( jqXHR.status + ' -- ' + errorThrown );});
      }
  } );
}

function ManageQuarantineEntry(params,obj) {
  if(obj){
      $(obj).css('color', '#00cc00');
  }

  params['posted'] = new Date().getTime();

  $.ajax('/admin/quarantine', {
      data: params,
      type: 'POST',
      dataType: 'json',
      success: function( data ) {
          ___loadFeedback(function() {feedBack.addFromJSON(data);});
      },
      error: function( jqXHR, statusText, errorThrown ) {
          ___loadFeedback(function() {feedBack.add( jqXHR.status + ' -- ' + errorThrown );});
      }
  });
}

function MarkEntrySticky( entryID, type, stickyChk ) {
  var params = '';
  var urlvalue = '';
  var chboxvalue = "";
  if( stickyChk.checked ) {
      params = "entryID=" + entryID
              + "&type=" + type;
      chboxvalue = 'on';
  }
  else {
      params = "entryID=" + entryID
              + "&type=" + type;
      chboxvalue = 'off';
  }

  $.ajax('/ajax/sticky', {
      data: params,
      type: 'POST',
      success: function( data ) {
          ___loadFeedback(function() {
              if( chboxvalue == 'on' ) {
                  feedBack.add("Sticky mark is set successfully.");
              }
              else if( chboxvalue == 'off' ) {
                  feedBack.add("Sticky mark is unset successfully.");
              }
          });
      },

      error: function( jqXHR, statusText, errorThrown ) {
          ___loadFeedback(function() {
            feedBack.clear ();
            feedBack.add (jqXHR.status + ' -- QUESTION objects are not sticky-able ' + errorThrown);
          });
      }
  });
}