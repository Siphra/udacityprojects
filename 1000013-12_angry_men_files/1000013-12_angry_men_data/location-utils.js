define(function() { return webpackJsonp([14,15],{

/***/ 563:
/***/ (function(module, exports, __webpack_require__) {

"use strict";


Object.defineProperty(exports, "__esModule", {
    value: true
});
exports.getLocationFromPlaceId = getLocationFromPlaceId;
exports.getLocation = getLocation;
exports.saveLocationPlaceId = saveLocationPlaceId;
exports.googleMapsAutocompleteSource = googleMapsAutocompleteSource;

var _bluebird = __webpack_require__(240);

var _bluebird2 = _interopRequireDefault(_bluebird);

var _superagent = __webpack_require__(111);

var _superagent2 = _interopRequireDefault(_superagent);

var _rtConfigDev = __webpack_require__(88);

var _rtConfigDev2 = _interopRequireDefault(_rtConfigDev);

function _interopRequireDefault(obj) { return obj && obj.__esModule ? obj : { default: obj }; }

if (!window.requirejs) {
    window.requirejs = function requirejs(thing, callback) {
        if (thing[0] === 'googleMapsApis') {
            callback(google);
        } else if (thing[0] === 'globals') {
            callback(_rtConfigDev2.default);
        }
    };
} /* global requirejs, google, window, document */


var LOCATION_LOCAL_STORAGE_KEY = 'location.place-id';

var placesService = void 0;
var autocompleteService = void 0;

function getPlacesServiceInstance() {
    if (!placesService) {
        placesService = new google.maps.places.PlacesService(document.getElementById('google-attributions'));
    }
    return placesService;
}

function getAutocompleteServiceInstance() {
    if (!autocompleteService) {
        autocompleteService = new google.maps.places.AutocompleteService();
    }
    return autocompleteService;
}

function getPlaceIdFromLocalStorage() {
    if (!window.localStorage) {
        return null;
    }
    return window.localStorage.getItem(LOCATION_LOCAL_STORAGE_KEY);
}

function transformPlaceToLocation(place) {
    return {
        displayName: place.name,
        latitude: place.geometry.location.lat(),
        longitude: place.geometry.location.lng(),
        placeId: place.place_id
    };
}

function initializeGoogleAutocomplete(input, locationPicker) {
    requirejs(['googleMapsApis'], function () {
        var googleAutocomplete = new google.maps.places.Autocomplete(input);
        googleAutocomplete.setFields(['name', 'geometry.location', 'place_id']);
        google.maps.event.addListener(googleAutocomplete, 'place_changed', function () {
            var place = googleAutocomplete.getPlace();
            var location = transformPlaceToLocation(place);
            locationPicker.applyNewLocation(location);
        });
    });
}
function getLocationFromPlaceId(placeId) {
    return new _bluebird2.default(function (resolve, reject) {
        requirejs(['googleMapsApis'], function () {
            getPlacesServiceInstance().getDetails({
                placeId: placeId,
                fields: ['name', 'geometry.location', 'place_id']
            }, function (place, status) {
                if (status === google.maps.places.PlacesServiceStatus.OK) {
                    resolve(place);
                } else {
                    reject(new Error('No place found in Google Places Service that matches placeId ' + placeId));
                }
            });
        });
    }).then(transformPlaceToLocation);
}

function getSavedLocation() {
    return new _bluebird2.default(function (resolve, reject) {
        var placeId = getPlaceIdFromLocalStorage();
        if (placeId) {
            getLocationFromPlaceId(placeId).then(function (location) {
                return resolve(location);
            }).catch(function (err) {
                return reject(err);
            });
        } else {
            reject(new Error('No placeId found in localStorage'));
        }
    });
}

function transformIpGeoDataToLocation(data) {
    return {
        displayName: data.city + ', ' + data.region,
        latitude: data.latitude,
        longitude: data.longitude
    };
}

function getLocationFromIp() {
    return new _bluebird2.default(function (resolve, reject) {
        requirejs(['globals'], function (RT) {
            _superagent2.default.get(RT.ShowtimesHost + '/ticketing/api/v1/geoip').end(function (err, res) {
                if (res && res.text && res.body && res.body.city && res.body.longitude) {
                    resolve(res.body);
                } else {
                    reject('Could not get location info by IP');
                }
            });
        });
    }).then(transformIpGeoDataToLocation);
}

/**
 * Attempts to get saved location (from localStorage), and falls back on geo ip
 * @returns {Promise.<T>|*}
 */
function getLocation() {
    return getSavedLocation().catch(function () {
        return getLocationFromIp();
    });
}

function saveLocationPlaceId(placeId) {
    if (window.localStorage && placeId) {
        window.localStorage.setItem(LOCATION_LOCAL_STORAGE_KEY, placeId);
    }
}

var GOOGLE_MAPS_PREDICTION_TYPES = ['geocode'];

function googleMapsAutocompleteSource() {
    return function (request, response) {
        requirejs(['googleMapsApis'], function () {
            getAutocompleteServiceInstance().getPlacePredictions({
                input: request.term,
                types: GOOGLE_MAPS_PREDICTION_TYPES
            }, function (predictions, status) {
                if (status === google.maps.places.PlacesServiceStatus.OK) {
                    response(predictions.map(function (prediction) {
                        return {
                            placeId: prediction.place_id,
                            label: prediction.description
                        };
                    }));
                }
            });
        });
    };
}

exports.default = {
    getLocation: getLocation,
    getLocationFromPlaceId: getLocationFromPlaceId,
    getPlaceIdFromLocalStorage: getPlaceIdFromLocalStorage,
    googleMapsAutocompleteSource: googleMapsAutocompleteSource,
    initializeGoogleAutocomplete: initializeGoogleAutocomplete,
    saveLocationPlaceId: saveLocationPlaceId
};

/***/ }),

/***/ 743:
/***/ (function(module, exports, __webpack_require__) {

"use strict";


Object.defineProperty(exports, "__esModule", {
    value: true
});

var _createClass = function () { function defineProperties(target, props) { for (var i = 0; i < props.length; i++) { var descriptor = props[i]; descriptor.enumerable = descriptor.enumerable || false; descriptor.configurable = true; if ("value" in descriptor) descriptor.writable = true; Object.defineProperty(target, descriptor.key, descriptor); } } return function (Constructor, protoProps, staticProps) { if (protoProps) defineProperties(Constructor.prototype, protoProps); if (staticProps) defineProperties(Constructor, staticProps); return Constructor; }; }();

var _react = __webpack_require__(1);

var _react2 = _interopRequireDefault(_react);

var _LocationUtils = __webpack_require__(563);

function _interopRequireDefault(obj) { return obj && obj.__esModule ? obj : { default: obj }; }

function _classCallCheck(instance, Constructor) { if (!(instance instanceof Constructor)) { throw new TypeError("Cannot call a class as a function"); } }

function _possibleConstructorReturn(self, call) { if (!self) { throw new ReferenceError("this hasn't been initialised - super() hasn't been called"); } return call && (typeof call === "object" || typeof call === "function") ? call : self; }

function _inherits(subClass, superClass) { if (typeof superClass !== "function" && superClass !== null) { throw new TypeError("Super expression must either be null or a function, not " + typeof superClass); } subClass.prototype = Object.create(superClass && superClass.prototype, { constructor: { value: subClass, enumerable: false, writable: true, configurable: true } }); if (superClass) Object.setPrototypeOf ? Object.setPrototypeOf(subClass, superClass) : subClass.__proto__ = superClass; } /* eslint-disable no-console */


__webpack_require__(956);

var berkeleyPlaceId = 'ChIJ00mFOjZ5hYARk-l1ppUV6pQ';
// const albanyPlaceId = 'ChIJPQVb0tJ4hYARLxEHP9E4sNU';

var MobShowtimes = function (_Component) {
    _inherits(MobShowtimes, _Component);

    function MobShowtimes() {
        _classCallCheck(this, MobShowtimes);

        return _possibleConstructorReturn(this, (MobShowtimes.__proto__ || Object.getPrototypeOf(MobShowtimes)).apply(this, arguments));
    }

    _createClass(MobShowtimes, [{
        key: 'componentDidMount',
        value: function componentDidMount() {
            (0, _LocationUtils.getLocationFromPlaceId)(berkeleyPlaceId).then(function (location) {
                console.info('got location from placeId(ChIJ00mFOjZ5hYARk-l1ppUV6pQ)!', location);
            }).catch(function (err) {
                console.error('failed to get location from placeId :(', err);
            });

            var source = (0, _LocationUtils.googleMapsAutocompleteSource)();

            source({ term: 'albany, ca' }, function (response) {
                console.info('here are the predictions', response);
            });
        }
    }, {
        key: 'render',
        value: function render() {
            var GeoIpHost = this.props.config.GeoIpHost;

            return _react2.default.createElement(
                'div',
                null,
                'MOB SHOWTIMES HERE! stay tuned. ',
                GeoIpHost
            );
        }
    }]);

    return MobShowtimes;
}(_react.Component);

MobShowtimes.propTypes = {
    config: _react.PropTypes.shape
};
exports.default = MobShowtimes;
module.exports = exports['default'];

/***/ }),

/***/ 842:
/***/ (function(module, exports, __webpack_require__) {

exports = module.exports = __webpack_require__(45)(undefined);
// imports


// module
exports.push([module.i, "", ""]);

// exports


/***/ }),

/***/ 956:
/***/ (function(module, exports, __webpack_require__) {

// style-loader: Adds some css to the DOM by adding a <style> tag

// load the styles
var content = __webpack_require__(842);
if(typeof content === 'string') content = [[module.i, content, '']];
// add the styles to the DOM
var update = __webpack_require__(47)(content, {});
if(content.locals) module.exports = content.locals;
// Hot Module Replacement
if(false) {
	// When the styles change, update the <style> tags
	if(!content.locals) {
		module.hot.accept("!!../../node_modules/css-loader/index.js!../../node_modules/sass-loader/lib/loader.js!./MobShowtimes.scss", function() {
			var newContent = require("!!../../node_modules/css-loader/index.js!../../node_modules/sass-loader/lib/loader.js!./MobShowtimes.scss");
			if(typeof newContent === 'string') newContent = [[module.id, newContent, '']];
			update(newContent);
		});
	}
	// When the module is disposed, remove the <style> tags
	module.hot.dispose(function() { update(); });
}

/***/ }),

/***/ 981:
/***/ (function(module, exports, __webpack_require__) {

"use strict";


__webpack_require__(25);

var _react = __webpack_require__(1);

var _react2 = _interopRequireDefault(_react);

var _reactDom = __webpack_require__(19);

var _reactDom2 = _interopRequireDefault(_reactDom);

var _LocationUtils = __webpack_require__(563);

var _LocationUtils2 = _interopRequireDefault(_LocationUtils);

var _MobShowtimes = __webpack_require__(743);

var _MobShowtimes2 = _interopRequireDefault(_MobShowtimes);

var _rtConfigDev = __webpack_require__(88);

var _rtConfigDev2 = _interopRequireDefault(_rtConfigDev);

function _interopRequireDefault(obj) { return obj && obj.__esModule ? obj : { default: obj }; }

/* global document */
if (false) {
    var showtimesRoot = document.getElementById('showtimes-root');
    _reactDom2.default.render(_react2.default.createElement(_MobShowtimes2.default, { config: _rtConfigDev2.default }), showtimesRoot);
}

module.exports = _LocationUtils2.default;

/***/ })

},[981])});;