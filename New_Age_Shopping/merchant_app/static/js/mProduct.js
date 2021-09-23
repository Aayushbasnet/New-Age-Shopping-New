// popup window

console.log("merchant dashboard!!");

$(function(){
    var hash = window.location.hash;
    hash && $('div.nav a[href="' + hash + '"]').tab('show');
    console.log(hash)
  
    $('.nav-pills a').click(function (e) {
      $(this).tab('show');
    //   var scrollmem = $('body').scrollTop();
      window.location.hash = this.hash;
    //   $('html,body').scrollTop(scrollmem);
    });
  });