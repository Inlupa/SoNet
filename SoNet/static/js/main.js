new Swiper('.image-slider',{
    navigation:{
        nextEl: '.swiper-button-next',
        prevEl: '.swiper-button-prev'
    },
    //возможность скроллить стрелочками клавиатуры
    keyboard:{
        enabled:true,
        onlyInViewport:true,
    },
    // возможномть скроллить колесом мыши
    mousewheel: {
        sensitivity: 1,
        eventsTarget: ".image-slider"
    },
    // автовысота слайда и бесконечная прокрутка
    loop: true,
    //автопрокрутка
    autoplay: {
        delay:5000,
    },
    //скорость изменения картинки
    speed:1000,
});





    async function getData(url, page, paginateBy) {
        const urlWithParams = url + "?" + new URLSearchParams({
            page: page,
            per_page: paginateBy
        })
        const response = await fetch(urlWithParams);
        return response.json();
    }

    class FauxPaginator {
        constructor(perPage) {
            this.perPage = perPage
            this.pageIndex = 1
            this.container = document.querySelector("#keywords")
            this.elements = document.querySelectorAll("pre")
            this.label = document.querySelector("#current")
            this.prev = document.querySelector("#prev")
            this.next = document.querySelector("#next")
            this.prev.addEventListener("click", this.onPrevClick.bind(this))
            this.next.addEventListener("click", this.onNextClick.bind(this))
            this.goToPage()
        }

        onPrevClick(event) {
            event.preventDefault()
            this.pageIndex--
            this.goToPage()
        }

        onNextClick(event) {
            event.preventDefault()
            this.pageIndex++
            this.goToPage()
        }
/*
        тут надо разобраться как добавить мои новости в элемент ниже
*/

        addElement(keyword) {
            const pre = document.createElement("div")
            pre.append(keyword)
            this.container.append(pre)
        }

        goToPage() {
            getData(".json", this.pageIndex, this.perPage)
                .then(response => {
                    this.container.innerHTML = '';
                    response.data.forEach((el) => {
                        this.addElement(el.news_name)
                        this.addElement(el.news_url)
                        this.addElement(el.pub_date)
                        this.addElement(el.news_anno)
                    });
                    this.label.innerText = this.pageIndex
                    const firstPage = this.pageIndex === 1
                    const lastPage = !response.page.has_next
                    this.prev.style.display = firstPage ? "none" : "inline-block"
                    this.next.style.display = lastPage ? "none" : "inline-block"
                });
        }
    }

    new FauxPaginator(3);


//$(function () {
//        // пагинация ajax
//        let now_page = 1;
//
//        $('.now_page').first().addClass('page_this');
//        // Предыдущий
//
//        $('.first_page').click(function () {
//            now_page =  now_page - 1;
//            if (now_page < 1) {
//                now_page = 1;
//                return false
//            } else {
//                $('.page_this').parent().prev().click();
//            }
//        });
//        //Следующая страница
//        $('.last_page').click(function () {
//            let num_pages = $('.now_page').last().text();
//            now_page = now_page + 1;
//            if (now_page > parseInt(num_pages)) {
//                now_page = now_page - 1;
//                return false
//            } else {
//                $('.page_this').parent().next().click();
//            }
//        });
//        // Переключить страницу
//        $('.now_page').click(function () {
//            now_page = parseInt($(this).children('button').text());
//            $('.now_page').removeClass('page_this')
//            $(this).addClass('page_this');
//            $(this).children('button').addClass('page_this');
//            page_click()
//        });
//
//        function page_click() {
//            let page_form = $('#page');
//            $.ajax({
//                type: 'get',
//                url: page_form.attr('action'),
//                data: {page: now_page},
//                success: function (data) {
//                    $('#tbody tr').remove();
//                    $('#num_pages').html('Все вместе' + data.num_pages + 'страница');
//
//                    $.each(data.news_li, function (index, news) {
//                        let a = '<td>';
//                        let b = '</td>';
//                        let body = a + news.news_name + b + a + news.news_anno + b + a + news.news_url + b;
//                        $('#tbody').append('<tr>' + body + '</tr>');
//                    });
//                }
//            })
//        }
//    })
