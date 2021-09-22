// to increase size of text area automatically while your type//

function auto_grow_user_comment_area(element) {
    element.style.height = 'auto';
    element.style.height = element.scrollHeight + 'px';
}
//for comment button//

let user_comment_area = document.querySelector('.user_comment_area textarea');
let comment_button_section = document.querySelector('.comment_button_section');
let cancel_button = document.getElementById('cancel_button');
let comment_button = document.getElementById('comment_button');
let user_comment_placeholder = user_comment_area.getAttribute('placeholder');


user_comment_area.onfocus = function () {
    this.setAttribute('placeholder', '');
    this.style.borderColor = '#333';
    comment_button_section.style.display = 'block';
}

user_comment_area.onblur = function () {
    this.setAttribute('placeholder', user_comment_placeholder);
    this.style.borderColor = '#aaa';
}

cancel_button.onclick = function () {
    comment_button_section.style.display = "none";
    user_comment_area.value = '';
    user_comment_area.style.height = '30px';
}

function comment_button_blue_background(element) {
    comment_button.style.backgroundColor = "#3ea6ff";
}

function comment_button_default_background(element) {
    comment_button.style.backgroundColor = "#606060";
}

// three vertical drop menu list in comment section
let edit_or_report_comment = document.querySelector('.edit_or_report_comment')

function three_vertical_dot_comment_menu(element) {
    if (edit_or_report_comment.style.display === 'block') {
        edit_or_report_comment.style.display = 'none';
    } else {
        edit_or_report_comment.style.display = 'block';
    }
}

edit_or_report_comment.onmouseenter = function () {
    edit_or_report_comment.style.display = 'block';
}

edit_or_report_comment.onmouseleave = function () {
    edit_or_report_comment.style.display = 'none';
}

// average user rating chart 
var rating_chart = document.getElementById('average_user_rating_chart').getContext('2d');
var average_user_rating_chart = new Chart(rating_chart, {
    type: 'bar',
    data: {
        labels:["5 star", "4 star", "3 star", "2 star", "1 star"],
        datasets:[{
            label:"This many people gave rating",
            backgroundColor:"gray",
            barThickness: 18,
            borderWidth: 1,
            borderRadius: 1,
            hoverBackgroundColor: 'green',
            data:[300,5000,1020,500,255],
        }]
    },

    options:{
        responsive: true,
        indexAxis:'y',

        scales: {
            

            x:{
                categoryPercentage: 1.5,   
                barPercentage:1.0, 
                display : false,
            },
            y:{
                ticks:{
                    color:'red',
                    font:{
                        size: 16,
                    },
                },

                grid:{
                    display: false,
                },  
            },
        },

        layout: {
            padding: 0,
        },

        plugins:{
            legend:{
                display:false,
                position:'right',
            },
            tooltip: {
                enabled: true,
            }
        },  

        elements:{
            radius: 10,
            rotation: 45,
        },
    }
});


//Alternative image selector

let main_display_image= document.getElementById('main_display_image');
let main_image= main_display_image.getAttribute('src');

let alternative_image1= document.getElementById('alternative_image1');
let img1=alternative_image1.getAttribute('src');

let alternative_image2= document.getElementById('alternative_image2');
let img2=alternative_image2.getAttribute('src');

let alternative_image3= document.getElementById('alternative_image3');
let img3=alternative_image3.getAttribute('src');

let alternative_image4= document.getElementById('alternative_image4');
let img4=alternative_image4.getAttribute('src');

alternative_image1.onclick=function(){
    alternative_image1.style.border='1px solid red';
    main_display_image.src= img1;
}

alternative_image2.onclick=function(){
    alternative_image2.style.border='1px solid red';
    main_display_image.src= img2;
}

alternative_image3.onclick=function(){
    alternative_image3.style.border='1px solid red';
    main_display_image.src= img3;
}

alternative_image4.onclick=function(){
    alternative_image4.style.border='1px solid red';
    main_display_image.src= img4;
}
