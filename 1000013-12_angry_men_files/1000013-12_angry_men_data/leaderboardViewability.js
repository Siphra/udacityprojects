define(["jquery","domReady!","bezier"],function(e){function a(a){if(0==a&&d.data("isSticky"))return d.removeClass("header_and_leaderboard_scroll"),e("#header-main").removeClass("header_main_scroll").css("margin-top","0px"),d.data("isSticky",!1),0;var r=Math.min(a/o,1),n=i.get(r),t=e("#top_leaderboard_wrapper").outerHeight();return 1100>e("leaderboard_top_ad").width()&&e("#header_and_leaderboard").css({width:"1100px"}),-n*t}function r(){if(d.data("isSticky")){var e=document.documentElement.scrollTop||document.body.scrollTop;d.css("top",a(e)+"px")}}var d=e("#header_and_leaderboard");d.addClass("header_and_leaderboard_scroll"),d.data("isSticky",!0),"0px"===e("#header-main").css("margin-top")&&e("#header-main").addClass("header_main_scroll");var o=1e3,i=BezierEasing(0,0,1,.5);window.addEventListener("scroll",function(){window.requestAnimationFrame(r)})});
//# sourceMappingURL=leaderboardViewability.jsp.min.js.map