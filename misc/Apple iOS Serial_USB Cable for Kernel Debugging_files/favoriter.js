var Favoriter;

Favoriter = (function() {

  function Favoriter(element) {
    var defaults;
    this.element = element;
    defaults = {
      entryId: null,
      isFavorite: false,
      alreadyFavoritedLink: false,
      notFavoritedLink: false,
      refreshPage: false
    };
    this.options = $.extend(defaults, arguments[1]);
    this.bindEvents().writeDisplay(this.options.isFavorite);
  }

  Favoriter.prototype.writeDisplay = function(bool) {
    this.element.empty();
    if (bool) {
      this.isFavorite = bool;
      if (this.options.alreadyFavoritedLink) {
        this.element.html('<a href="#"><img src="/static/img/fav-icon.png" alt="Remove from your favorites!"/>Un-fave</a>');
      } else {
        this.element.html('');
      }
    } else {
      this.isFavorite = bool;
      if (this.options.notFavoritedLink) {
        this.element.html('<a href="#"><img src="/static/img/fav-icon.png" alt="Make this a favorite!"/>Favorite</a>');
      } else {
        this.element.html('');
      }
    }
    return this;
  };

  Favoriter.prototype.bindEvents = function() {
    var _self;
    _self = this;
    this.element.click(function(evt) {
      var params;
      evt.preventDefault();
      _self.element.html('<img src="/static/img/spinner.gif" alt="Please wait while loading" />');
      params = {
        entryId: _self.options.entryId
      };
      return $.ajax({
        url: '/ajax/favorite',
        data: params,
        dataType: 'text',
        success: function(data, textStatus, jqXHR) {
          if (_self.options.refreshPage) {
            return window.location.reload(true);
          } else {
            return _self.writeDisplay(data === "true");
          }
        },
        error: function(jqXHR, textStatus, errorThrown) {
          alert('error: ' + textStatus + "\n" + errorThrown);
          return _self.writeDisplay(_self.isFavorite);
        }
      });
    });
    return this;
  };

  return Favoriter;

})();
