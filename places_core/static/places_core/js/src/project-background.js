//
// project-background.js
// =====================

// Ustawianie zdjęcia tła dla projektu.

require([window.STATIC_URL + "/js/config.js"], function () {
  require(['jquery',
           'js/modules/ui/image-form',
           'js/modules/common'],

  function($, ImageForm) {
      
    "use strict";
    
    $(document).ready(function () {
      var form = new ImageForm({
        $el: $('#project-background-form'),
        orientation: 'landscape'
      });
    });
    
    $(document).trigger('load');
      
  });
});