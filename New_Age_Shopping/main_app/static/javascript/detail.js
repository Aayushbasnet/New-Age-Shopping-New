
// detai and review switch

$(function () {
  var hash = window.location.hash;
  hash && $('ul.nav a[href="' + hash + '"]').tab('show');
  console.log(hash)

  $('.nav-pills a').click(function (e) {
    $(this).tab('show');
    //   var scrollmem = $('body').scrollTop();
    window.location.hash = this.hash;
    //   $('html,body').scrollTop(scrollmem);
  });
});

//alternative image
const subImage = document.querySelectorAll(".image-change-js");
const mainImage = document.querySelector(".main-image");
const mainImageContainer = document.querySelector(".main-image-layout");


subImage.forEach((item, index) => {

  var flag = true;
  if (flag) {
    flag = false;
    biggerImage = mainImage.src
    console.log(biggerImage)
  }

  item.onclick = () => {
    mainImage.src = item.src;
  }
  // item.onmouseout = () => {
  //   console.log("I am out!!!")
  //   mainImage.src = biggerImage
  // }
});

//comment display

const seeMoreBtn = document.querySelector('.see_more_btn');
const hide_comment = document.querySelector('.hide_comment');

seeMoreBtn.addEventListener('click', (e)=>{
    if(seeMoreBtn.innerText ==="See more >>"){
      seeMoreBtn.innerText ='See less <<';
      hide_comment.style.height = 'fit-content';
    }
    else{
      hide_comment.style.height = '350px';
      seeMoreBtn.innerText ='See more >>';
    }
    console.log("clicked")
})