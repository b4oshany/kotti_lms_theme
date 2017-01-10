(function (root, factory) {
  if (typeof define === 'function' && define.amd) {
    // AMD. Register as an anonymous module.
    define([], function () {
      return (root.returnExportsGlobal = factory());
    });
  } else if (typeof exports === 'object') {
    // Node. Does not work with strict CommonJS, but
    // only CommonJS-like enviroments that support module.exports,
    // like Node.
    module.exports = factory();
  } else {
    root['Chartist.plugins.ctoBarLabels'] = factory();
  }
}(this, function () {

  /**
   * Chartist.js plugin to display a data label left or right to a bar chart column.
   *
   */
  /* global Chartist */
  (function(window, document, Chartist) {
    'use strict';

      var defaultOptions = {
          labelClass: 'ct-label',
          labelOffset: {
              x: 20,
              y: -4
          },
          barAnchor: 'left',
          labelPrefix: '',
          labelSuffix: ''
      };

      Chartist.plugins = Chartist.plugins || {};
      Chartist.plugins.ctoBarLabels = function(options) {

      options = Chartist.extend({}, defaultOptions, options);

      return function ctoBarLabels(chart) {
          // bar labels
          if(chart instanceof Chartist.Bar) {
              chart.on('draw', function(data) {
                  data.centerPos = (data.y1 + data.y2)/2;
                  if(data.type === (options.gType || 'bar' )) {
                    if(options.func != undefined){
                      options.func(data, options);
                    }else{
                      var value = parseInt(data.series[data.index]);
                      if(value == 100){
                        value = ""
                      }
                      data.group.elem('text', {
                          x: data.x2 + options.labelOffset.x,
                          y: data.centerPos - options.labelOffset.y,
                          style: 'font-size: 8pt; text-anchor: ' + options.barAnchor
                      }, options.labelClass).text(value);
                    }
                  }
              });
          }
      };
    };

  }(window, document, Chartist));
  return Chartist.plugins.ctoBarLabels;

}));
