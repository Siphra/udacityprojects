define(function() { return webpackJsonp([11,15],{

/***/ 753:
/***/ (function(module, exports, __webpack_require__) {

"use strict";


Object.defineProperty(exports, "__esModule", {
    value: true
});

var _extends = Object.assign || function (target) { for (var i = 1; i < arguments.length; i++) { var source = arguments[i]; for (var key in source) { if (Object.prototype.hasOwnProperty.call(source, key)) { target[key] = source[key]; } } } return target; };

var _createClass = function () { function defineProperties(target, props) { for (var i = 0; i < props.length; i++) { var descriptor = props[i]; descriptor.enumerable = descriptor.enumerable || false; descriptor.configurable = true; if ("value" in descriptor) descriptor.writable = true; Object.defineProperty(target, descriptor.key, descriptor); } } return function (Constructor, protoProps, staticProps) { if (protoProps) defineProperties(Constructor.prototype, protoProps); if (staticProps) defineProperties(Constructor, staticProps); return Constructor; }; }();

var _react = __webpack_require__(1);

var _react2 = _interopRequireDefault(_react);

var _classnames = __webpack_require__(17);

var _classnames2 = _interopRequireDefault(_classnames);

var _Carousel = __webpack_require__(237);

var _Carousel2 = _interopRequireDefault(_Carousel);

var _VideosCarouselItem = __webpack_require__(820);

var _VideosCarouselItem2 = _interopRequireDefault(_VideosCarouselItem);

function _interopRequireDefault(obj) { return obj && obj.__esModule ? obj : { default: obj }; }

function _classCallCheck(instance, Constructor) { if (!(instance instanceof Constructor)) { throw new TypeError("Cannot call a class as a function"); } }

function _possibleConstructorReturn(self, call) { if (!self) { throw new ReferenceError("this hasn't been initialised - super() hasn't been called"); } return call && (typeof call === "object" || typeof call === "function") ? call : self; }

function _inherits(subClass, superClass) { if (typeof superClass !== "function" && superClass !== null) { throw new TypeError("Super expression must either be null or a function, not " + typeof superClass); } subClass.prototype = Object.create(superClass && superClass.prototype, { constructor: { value: subClass, enumerable: false, writable: true, configurable: true } }); if (superClass) Object.setPrototypeOf ? Object.setPrototypeOf(subClass, superClass) : subClass.__proto__ = superClass; } /* global window */


__webpack_require__(964);

var VideosCarousel = function (_Component) {
    _inherits(VideosCarousel, _Component);

    function VideosCarousel() {
        _classCallCheck(this, VideosCarousel);

        return _possibleConstructorReturn(this, (VideosCarousel.__proto__ || Object.getPrototypeOf(VideosCarousel)).apply(this, arguments));
    }

    _createClass(VideosCarousel, [{
        key: 'render',
        value: function render() {
            var _props = this.props,
                videos = _props.videos,
                config = _props.config,
                mobileSetting = _props.mobileSetting,
                desktopSetting = _props.desktopSetting,
                mpxConfig = _props.mpxConfig,
                mpxFWSite = _props.mpxFWSite,
                mpxAccountPId = _props.mpxAccountPId,
                mpxPlayerPid = _props.mpxPlayerPid,
                mpxAccountId = _props.mpxAccountId;

            return _react2.default.createElement(
                _Carousel2.default,
                {
                    className: 'VideosCarousel',
                    mobileSetting: mobileSetting,
                    desktopSetting: desktopSetting
                },
                videos.map(function (video) {
                    return _react2.default.createElement(
                        'div',
                        { key: video.id },
                        _react2.default.createElement(_VideosCarouselItem2.default, _extends({
                            config: config
                        }, video, {
                            trackVideoClick: VideosCarousel.trackVideoClick,
                            linkClassName: (0, _classnames2.default)('VideosCarousel__item-link', 'trailer_play_action_button'),
                            mpxParam: mpxConfig,
                            mpxFWSite: mpxFWSite,
                            mpxAccountpid: mpxAccountPId,
                            mpxPlayerpid: mpxPlayerPid,
                            mpxAccountid: mpxAccountId
                        }))
                    );
                })
            );
        }
    }], [{
        key: 'trackVideoClick',
        value: function trackVideoClick(id) {
            if (window.ga) {
                window.ga('gtmTracker.send', 'pageview', window.location.pathname + '/modal/videos/' + id);
            }
        }
    }]);

    return VideosCarousel;
}(_react.Component);

VideosCarousel.propTypes = {
    videos: _react.PropTypes.arrayOf(_react.PropTypes.shape({
        id: _react.PropTypes.string.isRequired,
        thumbUrl: _react.PropTypes.string,
        title: _react.PropTypes.string,
        duration: _react.PropTypes.number,
        guid: _react.PropTypes.string.isRequired
    })),
    config: _react.PropTypes.shape({
        StaticHost: _react.PropTypes.string
    }),
    mobileSetting: _react.PropTypes.shape({
        slidesToShow: _react.PropTypes.number.isRequired,
        slidesToScroll: _react.PropTypes.number.isRequired
    }),
    desktopSetting: _react.PropTypes.shape({
        slidesToShow: _react.PropTypes.number.isRequired,
        slidesToScroll: _react.PropTypes.number.isRequired
    }),
    mpxConfig: _react.PropTypes.string,
    mpxFWSite: _react.PropTypes.string,
    mpxAccountPId: _react.PropTypes.string,
    mpxPlayerPid: _react.PropTypes.string,
    mpxAccountId: _react.PropTypes.string
};
exports.default = VideosCarousel;
module.exports = exports['default'];

/***/ }),

/***/ 820:
/***/ (function(module, exports, __webpack_require__) {

"use strict";


Object.defineProperty(exports, "__esModule", {
    value: true
});

var _createClass = function () { function defineProperties(target, props) { for (var i = 0; i < props.length; i++) { var descriptor = props[i]; descriptor.enumerable = descriptor.enumerable || false; descriptor.configurable = true; if ("value" in descriptor) descriptor.writable = true; Object.defineProperty(target, descriptor.key, descriptor); } } return function (Constructor, protoProps, staticProps) { if (protoProps) defineProperties(Constructor.prototype, protoProps); if (staticProps) defineProperties(Constructor, staticProps); return Constructor; }; }();

var _react = __webpack_require__(1);

var _react2 = _interopRequireDefault(_react);

var _leftPad = __webpack_require__(890);

var _leftPad2 = _interopRequireDefault(_leftPad);

function _interopRequireDefault(obj) { return obj && obj.__esModule ? obj : { default: obj }; }

function _classCallCheck(instance, Constructor) { if (!(instance instanceof Constructor)) { throw new TypeError("Cannot call a class as a function"); } }

function _possibleConstructorReturn(self, call) { if (!self) { throw new ReferenceError("this hasn't been initialised - super() hasn't been called"); } return call && (typeof call === "object" || typeof call === "function") ? call : self; }

function _inherits(subClass, superClass) { if (typeof superClass !== "function" && superClass !== null) { throw new TypeError("Super expression must either be null or a function, not " + typeof superClass); } subClass.prototype = Object.create(superClass && superClass.prototype, { constructor: { value: subClass, enumerable: false, writable: true, configurable: true } }); if (superClass) Object.setPrototypeOf ? Object.setPrototypeOf(subClass, superClass) : subClass.__proto__ = superClass; }

var VideosCarouselItem = function (_Component) {
    _inherits(VideosCarouselItem, _Component);

    function VideosCarouselItem() {
        var _ref;

        var _temp, _this, _ret;

        _classCallCheck(this, VideosCarouselItem);

        for (var _len = arguments.length, args = Array(_len), _key = 0; _key < _len; _key++) {
            args[_key] = arguments[_key];
        }

        return _ret = (_temp = (_this = _possibleConstructorReturn(this, (_ref = VideosCarouselItem.__proto__ || Object.getPrototypeOf(VideosCarouselItem)).call.apply(_ref, [this].concat(args))), _this), _this.handleClick = function () {
            _this.props.trackVideoClick(_this.props.id);
        }, _temp), _possibleConstructorReturn(_this, _ret);
    }

    _createClass(VideosCarouselItem, [{
        key: 'render',
        value: function render() {
            var _props = this.props,
                config = _props.config,
                duration = _props.duration,
                id = _props.id,
                linkClassName = _props.linkClassName,
                noAds = _props.noAds,
                thumbUrl = _props.thumbUrl,
                title = _props.title,
                guid = _props.guid,
                mpxParam = _props.mpxParam,
                mpxFWSite = _props.mpxFWSite,
                mpxAccountpid = _props.mpxAccountpid,
                mpxPlayerpid = _props.mpxPlayerpid,
                mpxAccountid = _props.mpxAccountid;

            var NO_IMAGE_AVAILABLE_THUMBNAIL = config.StaticHost + '/static/images/defaults/video.default.l.jpg';
            return (
                // This component represents each individual child of a set of children
                // passed into Slick. Slick needs several props passed down (data-index,
                // className) to render function correctly, so we pass them with the
                // spread operator (...this.props).
                _react2.default.createElement(
                    'div',
                    { className: 'VideosCarousel__item' },
                    _react2.default.createElement(
                        'a',
                        {
                            className: linkClassName,
                            'data-guid': guid,
                            'data-no-ads': noAds || false,
                            'data-video-id': id,
                            'data-title': title,
                            'data-mpx-params': mpxParam,
                            'data-mpx-fwsite': mpxFWSite,
                            'data-mpx-accountpid': mpxAccountpid,
                            'data-mpx-playerpid': mpxPlayerpid,
                            'data-mpx-accountid': mpxAccountid,
                            onClick: this.handleClick
                        },
                        _react2.default.createElement(
                            'div',
                            { className: 'VideosCarousel__image-container' },
                            _react2.default.createElement('img', {
                                role: 'presentation',
                                className: 'VideosCarousel__image',
                                src: thumbUrl || NO_IMAGE_AVAILABLE_THUMBNAIL
                            }),
                            _react2.default.createElement(
                                'div',
                                { className: 'playButton' },
                                _react2.default.createElement('span', { className: 'glyphicon glyphicon-play light-translucent white' })
                            ),
                            duration && duration > 0 ? _react2.default.createElement(
                                'div',
                                { className: 'VideoCarousel__duration' },
                                VideosCarouselItem.formatDuration(duration)
                            ) : _react2.default.createElement('div', null)
                        ),
                        title && _react2.default.createElement(
                            'div',
                            { className: 'VideosCarousel__video-title' },
                            title
                        )
                    )
                )
            );
        }
    }], [{
        key: 'formatDuration',
        value: function formatDuration(durationInSeconds) {
            var date = new Date(null);
            date.setSeconds(durationInSeconds);
            return date.getUTCMinutes() + ':' + (0, _leftPad2.default)(date.getUTCSeconds(), 2, 0);
        }
    }]);

    return VideosCarouselItem;
}(_react.Component);

VideosCarouselItem.propTypes = {
    config: _react.PropTypes.shape({
        StaticHost: _react.PropTypes.string
    }),
    duration: _react.PropTypes.number.isRequired,
    guid: _react.PropTypes.string.isRequired,
    id: _react.PropTypes.string.isRequired,
    linkClassName: _react.PropTypes.string.isRequired,
    noAds: _react.PropTypes.bool,
    thumbUrl: _react.PropTypes.string.isRequired,
    trackVideoClick: _react.PropTypes.func.isRequired,
    title: _react.PropTypes.string.isRequired,
    mpxParam: _react.PropTypes.string,
    mpxFWSite: _react.PropTypes.string,
    mpxAccountpid: _react.PropTypes.string,
    mpxPlayerpid: _react.PropTypes.string,
    mpxAccountid: _react.PropTypes.string
};
exports.default = VideosCarouselItem;
module.exports = exports['default'];

/***/ }),

/***/ 851:
/***/ (function(module, exports, __webpack_require__) {

exports = module.exports = __webpack_require__(45)(undefined);
// imports


// module
exports.push([module.i, "#videos-carousel-root {\n  margin: auto -8px; }\n  @media (max-width: 767px) {\n    #videos-carousel-root {\n      margin-left: 0;\n      margin-right: 0;\n      margin-right: -20vw; }\n      #videos-carousel-root .slick-list {\n        max-width: 95vw;\n        overflow: hidden; } }\n\n.VideosCarousel .CarouselButton {\n  -moz-transform: translateY(-50%);\n  -o-transform: translateY(-50%);\n  -ms-transform: translateY(-50%);\n  -webkit-transform: translateY(-50%);\n  transform: translateY(-50%);\n  top: 50%; }\n\n.VideosCarousel__item {\n  cursor: pointer;\n  padding: 5px; }\n\n.VideosCarousel__item-link {\n  display: block; }\n  @media (min-width: 768px) {\n    .VideosCarousel__item-link:hover .VideosCarousel__image {\n      -moz-transform: scale3d(1.1, 1.1, 1);\n      -o-transform: scale3d(1.1, 1.1, 1);\n      -ms-transform: scale3d(1.1, 1.1, 1);\n      -webkit-transform: scale3d(1.1, 1.1, 1);\n      transform: scale3d(1.1, 1.1, 1); } }\n  .VideosCarousel__item-link:hover {\n    text-decoration: none; }\n  .VideosCarousel__item-link:active, .VideosCarousel__item-link:focus {\n    background-color: inherit;\n    text-decoration: none; }\n\n.VideosCarousel__slide-play-icon {\n  -webkit-filter: drop-shadow(2px 2px 7px rgba(0, 0, 0, 0.5));\n  -moz-filter: drop-shadow(2px 2px 7px rgba(0, 0, 0, 0.5));\n  -ms-filter: drop-shadow(2px 2px 7px rgba(0, 0, 0, 0.5));\n  -o-filter: drop-shadow(2px 2px 7px rgba(0, 0, 0, 0.5));\n  filter: drop-shadow(2px 2px 7px rgba(0, 0, 0, 0.5));\n  -moz-transition: opacity 0.15s ease-in-out;\n  -o-transition: opacity 0.15s ease-in-out;\n  -webkit-transition: opacity 0.15s ease-in-out;\n  transition: opacity 0.15s ease-in-out;\n  bottom: 2px;\n  color: white;\n  opacity: 0.6;\n  position: absolute;\n  right: 2px; }\n\n.VideosCarousel__item-link:hover .VideosCarousel__slide-play-icon {\n  opacity: 1; }\n\n.VideosCarousel__image-container {\n  position: relative;\n  overflow: hidden; }\n  .VideosCarousel__image-container .playButton {\n    position: absolute;\n    bottom: 7px;\n    right: 7px;\n    font-size: 35px;\n    height: 35px;\n    width: 35px; }\n  .VideosCarousel__image-container:hover .playButton .light-translucent {\n    opacity: 1; }\n\n.VideosCarousel__image {\n  -moz-transition: transform 0.15s ease-in-out;\n  -o-transition: transform 0.15s ease-in-out;\n  -webkit-transition: transform 0.15s ease-in-out;\n  transition: transform 0.15s ease-in-out; }\n\n.VideosCarousel__video-title {\n  color: #444;\n  display: -webkit-box;\n  font-size: 14px;\n  line-height: 1.2;\n  max-height: 2.4em;\n  padding: 5px 0;\n  text-overflow: ellipsis;\n  -webkit-box-orient: vertical;\n  -webkit-line-clamp: 2; }\n\n.VideoCarousel__duration {\n  position: absolute;\n  color: white;\n  font-weight: bolder;\n  bottom: 102px;\n  left: 125px;\n  padding: 2px 5px;\n  border-radius: 6px;\n  font-family: 'Franklin Gothic Book';\n  background: rgba(0, 0, 0, 0.5); }\n\n.VideosCarousel .CarouselButton {\n  top: 71px !important; }\n\n.VideosCarousel__video-title {\n  font-family: 'Franklin Gothic Book';\n  font-size: 16px; }\n\n.Carousel .slick-dots li.slick-active button {\n  background: #FA320A !important; }\n", ""]);

// exports


/***/ }),

/***/ 890:
/***/ (function(module, exports, __webpack_require__) {

"use strict";
/* This program is free software. It comes without any warranty, to
     * the extent permitted by applicable law. You can redistribute it
     * and/or modify it under the terms of the Do What The Fuck You Want
     * To Public License, Version 2, as published by Sam Hocevar. See
     * http://www.wtfpl.net/ for more details. */

module.exports = leftPad;

var cache = [
  '',
  ' ',
  '  ',
  '   ',
  '    ',
  '     ',
  '      ',
  '       ',
  '        ',
  '         '
];

function leftPad (str, len, ch) {
  // convert `str` to `string`
  str = str + '';
  // `len` is the `pad`'s length now
  len = len - str.length;
  // doesn't need to pad
  if (len <= 0) return str;
  // `ch` defaults to `' '`
  if (!ch && ch !== 0) ch = ' ';
  // convert `ch` to `string`
  ch = ch + '';
  // cache common use cases
  if (ch === ' ' && len < 10) return cache[len] + str;
  // `pad` starts with an empty string
  var pad = '';
  // loop
  while (true) {
    // add `ch` to `pad` if `len` is odd
    if (len & 1) pad += ch;
    // divide `len` by 2, ditch the remainder
    len >>= 1;
    // "double" the `ch` so this operation count grows logarithmically on `len`
    // each time `ch` is "doubled", the `len` would need to be "doubled" too
    // similar to finding a value in binary search tree, hence O(log(n))
    if (len) ch += ch;
    // `len` is 0, exit the loop
    else break;
  }
  // pad `str`!
  return pad + str;
}


/***/ }),

/***/ 964:
/***/ (function(module, exports, __webpack_require__) {

// style-loader: Adds some css to the DOM by adding a <style> tag

// load the styles
var content = __webpack_require__(851);
if(typeof content === 'string') content = [[module.i, content, '']];
// add the styles to the DOM
var update = __webpack_require__(47)(content, {});
if(content.locals) module.exports = content.locals;
// Hot Module Replacement
if(false) {
	// When the styles change, update the <style> tags
	if(!content.locals) {
		module.hot.accept("!!../../node_modules/css-loader/index.js!../../node_modules/sass-loader/lib/loader.js!./VideosCarousel.scss", function() {
			var newContent = require("!!../../node_modules/css-loader/index.js!../../node_modules/sass-loader/lib/loader.js!./VideosCarousel.scss");
			if(typeof newContent === 'string') newContent = [[module.id, newContent, '']];
			update(newContent);
		});
	}
	// When the module is disposed, remove the <style> tags
	module.hot.dispose(function() { update(); });
}

/***/ }),

/***/ 989:
/***/ (function(module, exports, __webpack_require__) {

"use strict";


__webpack_require__(25);

var _react = __webpack_require__(1);

var _react2 = _interopRequireDefault(_react);

var _reactDom = __webpack_require__(19);

var _reactDom2 = _interopRequireDefault(_reactDom);

var _VideosCarousel = __webpack_require__(753);

var _VideosCarousel2 = _interopRequireDefault(_VideosCarousel);

var _rtConfigDev = __webpack_require__(88);

var _rtConfigDev2 = _interopRequireDefault(_rtConfigDev);

function _interopRequireDefault(obj) { return obj && obj.__esModule ? obj : { default: obj }; }

function mount(element, videos, mobileSetting, desktopSetting, mpx, mpxFWSite, mpxAccountPId, mpxPlayerPid, mpxAccountId) {
    if (!element) {
        throw new Error('Could not find videos root to attach videos component');
    }

    if (false) {
        _reactDom2.default.render(_react2.default.createElement(_VideosCarousel2.default, {
            config: _rtConfigDev2.default,
            videos: videos,
            mobileSetting: mobileSetting,
            desktopSetting: desktopSetting,
            mpxConfig: mpx,
            mpxFWSite: mpxFWSite,
            mpxAccountPId: mpxAccountPId,
            mpxPlayerPid: mpxPlayerPid,
            mpxAccountId: mpxAccountId
        }), element);
    } else {
        requirejs(['globals'], function (RT) {
            _reactDom2.default.render(_react2.default.createElement(_VideosCarousel2.default, {
                config: RT,
                videos: videos,
                mobileSetting: mobileSetting,
                desktopSetting: desktopSetting,
                mpxConfig: mpx,
                mpxFWSite: mpxFWSite,
                mpxAccountPId: mpxAccountPId,
                mpxPlayerPid: mpxPlayerPid,
                mpxAccountId: mpxAccountId
            }), element);
        });
    }
} /* global requirejs, document, window */


module.exports = mount;

if (false) {
    mount(document.getElementById('videos-carousel-root'), window.videos, { slidesToShow: 4, slidesToScroll: 4 }, { slidesToShow: 2, slidesToScroll: 2 });
}

/***/ })

},[989])});;