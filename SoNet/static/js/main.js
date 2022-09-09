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


    /*async function getData(url, page, paginateBy) {
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

        addElement(keyword) {

            const pre = document.ch

            pre.append(keyword)

            this.container.appendChild(pre)
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

    new FauxPaginator(3);*/



    class ItcAccordion {
      constructor(target, config) {
        this._el = typeof target === 'string' ? document.querySelector(target) : target;
        const defaultConfig = {
          alwaysOpen: true,
          duration: 350
        };
        this._config = Object.assign(defaultConfig, config);
        this.addEventListener();
      }
      addEventListener() {
        this._el.addEventListener('click', (e) => {
          const elHeader = e.target.closest('.accordion__header');
          if (!elHeader) {
            return;
          }
          if (!this._config.alwaysOpen) {
            const elOpenItem = this._el.querySelector('.accordion__item_show');
            if (elOpenItem) {
              elOpenItem !== elHeader.parentElement ? this.toggle(elOpenItem) : null;
            }
          }
          this.toggle(elHeader.parentElement);
        });
      }
      show(el) {
        const elBody = el.querySelector('.accordion__body');
        if (elBody.classList.contains('collapsing') || el.classList.contains('accordion__item_show')) {
          return;
        }
        elBody.style['display'] = 'block';
        const height = elBody.offsetHeight;
        elBody.style['height'] = 0;
        elBody.style['overflow'] = 'hidden';
        elBody.style['transition'] = `height ${this._config.duration}ms ease`;
        elBody.classList.add('collapsing');
        el.classList.add('accordion__item_slidedown');
        elBody.offsetHeight;
        elBody.style['height'] = `${height}px`;
        window.setTimeout(() => {
          elBody.classList.remove('collapsing');
          el.classList.remove('accordion__item_slidedown');
          elBody.classList.add('collapse');
          el.classList.add('accordion__item_show');
          elBody.style['display'] = '';
          elBody.style['height'] = '';
          elBody.style['transition'] = '';
          elBody.style['overflow'] = '';
        }, this._config.duration);
      }
      hide(el) {
        const elBody = el.querySelector('.accordion__body');
        if (elBody.classList.contains('collapsing') || !el.classList.contains('accordion__item_show')) {
          return;
        }
        elBody.style['height'] = `${elBody.offsetHeight}px`;
        elBody.offsetHeight;
        elBody.style['display'] = 'block';
        elBody.style['height'] = 0;
        elBody.style['overflow'] = 'hidden';
        elBody.style['transition'] = `height ${this._config.duration}ms ease`;
        elBody.classList.remove('collapse');
        el.classList.remove('accordion__item_show');
        elBody.classList.add('collapsing');
        window.setTimeout(() => {
          elBody.classList.remove('collapsing');
          elBody.classList.add('collapse');
          elBody.style['display'] = '';
          elBody.style['height'] = '';
          elBody.style['transition'] = '';
          elBody.style['overflow'] = '';
        }, this._config.duration);
      }
      toggle(el) {
        el.classList.contains('accordion__item_show') ? this.hide(el) : this.show(el);
      }
    }

    new ItcAccordion(document.querySelector('.accordion'), {
      alwaysOpen: true
    });

