function preDomPoll(){function e(){var e,o,i=this.parentNode.parentNode;for(e=0;e<i.childNodes.length;e+=1)o=i.childNodes[e],"LI"===o.nodeName.toUpperCase()&&o.classList&&o.querySelector("a").classList.remove("active");this.classList.add("active")}var o,i=document.getElementById("nav-list").getElementsByTagName("a"),t=location.href.split("#")[0];for(o=0;o<i.length;o+=1)i[o].href.split("#")[0]===t&&i[o].href!==t+"#"&&i[o].classList.add("active"),i[o].addEventListener&&(i[o].onclick=e)}function menuToggle(){["menu-btn","mobile-signup-btn","mobile-login-btn"].forEach(function(e){var o=document.getElementById("mobile-nav");document.getElementById(e).addEventListener("click",function(){o.classList.contains("menu-opened")?(o.classList.remove("menu-opened"),document.body.classList.remove("noscroll")):(o.classList.add("menu-opened"),document.body.classList.add("noscroll")),preDomPoll()})})}function poll(){if(document&&document.getElementById("nav-list"))return void preDomPoll();setTimeout(poll,10)}menuToggle(),poll(),define(["jquery","globals","underscore","backbone","js-cookie","bootstrap","rtClamp"],function(e,o,i,t,l){return i.templateSettings={interpolate:/\<\@\=(.+?)\@\>/gim,evaluate:/\<\@(.+?)\@\>/gim},function(t){!function(){var e=l.get("pvc"),o=new Date;o.setTime(o.getTime()+36e5),e&&l.set("pvc",parseInt(e)+1,{path:"/",expires:o})}(),function(){o.loginInit.always(function(){require([o.StaticHost+"/static/dist/app/views/LoginView.min.js"],function(t){o.loginView=new t.LoginModal({model:o.loginModel,LoginModalTemplate:i.template(e("script.LoginModalTemplate").html())}),o.loginView.render(),o.loginView.$el.attr("id","login"),o.loginView.$el.attr("role","dialog"),e("body").append(o.loginView.$el),o.signupView=new t.SignupModal({model:o.loginModel,SignupModalTemplate:i.template(e("script.SignupModalTemplate").html())}),o.signupView.render(),o.signupView.$el.attr("id","signup"),o.signupView.$el.attr("role","dialog"),e("body").append(o.signupView.$el),o.passwordView=new t.PasswordModal({PasswordModalTemplate:i.template(e("script.PasswordModalTemplate").html())}),o.passwordView.render(),o.passwordView.$el.attr("id","forgot-password"),o.passwordView.$el.attr("role","dialog"),e("body").append(o.passwordView.$el),o.desktopHeaderLogin=new t.DesktopLoginArea({model:o.loginModel,PageHeaderLoginTemplate:i.template(e("script.PageHeaderLoginTemplate").html())}),o.desktopHeaderLogin.render(),e("#headerUserSection").html(o.desktopHeaderLogin.$el),o.mobileHeaderLogin=new t.MobileLoginArea({model:o.loginModel,PageHeaderLoginMobileTemplate:i.template(e("script.PageHeaderLoginMobileTemplate").html())}),o.mobileHeaderLogin.render(),e("#navMenu .loginArea").html(o.mobileHeaderLogin.$el),o.loginModel.reloadSignIn(),o.loginViewLoad.resolve();var l=function(){e("#navMenu").hasClass("in")&&e("#navMenu").modal("toggle")};o.loginModel.addPersistAlwaysSignInCallback(l)})})}(),function(){e("[data-toggle='tooltip']").tooltip({template:'<div class="tooltip" role="tooltip"><div class="tooltip-arrow"></div><div class="tooltip-inner"></div></div>'})}(),require([o.StaticHost+"/static/dist/app/views/SocialTool.min.js"],function(o){var l={SocialToolTemplate:i.template(e("script.SocialToolsTemplate").html())};t&&(l.movieId=t);var n=new o(l);n.render(),e("body").append(n.$el)}.bind(this)),require(["domReady!"],function(){!function(){o.loginInit.always(function(){o.loginModel.addOneSignInCallback(function(o){if(o&&o.roles){var t=o.roles.reduce(function(e,o){return e[o]=!0,e},{}),l=e(".admin_panel");l&&l.length>0&&(e(".admin_panel").html(i.template(e("#adminPanelTemplate").html())({roles:t})),o&&o.isCritic&&e("#critics-add-article")&&e("#critics-add-article").show())}})})}()})}});
//# sourceMappingURL=bodyScript.tag.min.js.map