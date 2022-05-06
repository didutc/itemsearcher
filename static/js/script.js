console.log('i go')
$('.btn').click(function () {
    collect(this);

});
function newpage(id){
    window.open('https://search.shopping.naver.com/search/all?query='+id.innerText+''); 
    window.open('https://www.coupang.com/np/search?component=&q='+id.innerText+''); 
    console.log(id.innerText)

  }
$('.btnclose').click(function () {
    for (var i = 0; i < webwindow.length; i++) {
        webwindow[i].close()
    }
    // for (var i in webwindow) {
    //     i.close()
    // }


});
function collect(removeButton) {
    /* Remove row from DOM and recalc cart total */
    //  product 하나의 큰 div를 뜻함

    var productRow = $(removeButton).parent().prevAll('#name')
    var itemname = productRow.html()
    var url = '/transe/'
    var rep = fetch(url, {
        method: 'POST',
        headers: {
            'Content-type': 'application/json',
            // 'X-CSRFToken':csrftoken,
        },
        body: JSON.stringify(itemname)
    })
        .then((res) => {
            return res.json();
        })
        .then((data) => {

            return (data)
        });
    const printAddress = () => {
        rep.then((a) => {
            var x = a
            webwindow = [];

            webwindow.push(window.open("https://www.google.com/search?q=" + x[0] + "&source=lnms&tbm=isch&sa"))

            webwindow.push(window.open("https://www.google.com/search?q=" + x[1] + "&source=lnms&tbm=isch&sa"))

            webwindow.push(window.open("https://www.google.com/search?q=" + x[2] + "&source=lnms&tbm=isch&sa"))
            console.log('not working')
            webwindow.push(window.open("https://minne.com/category/saleonly/stationery?sort=none&input_method=typing&q=" + x[2]))

            // webwindow.push(window.open("https://www.google.com/search?q=" + x[0] + "&source=lnms&tbm=isch&sa"))
            // window.open("https://www.google.com/search?q=" + x[1] + "&source=lnms&tbm=isch&sa")
            // window.open("https://www.google.com/search?q=" + x[2] + "&source=lnms&tbm=isch&sa")
            // window.open("https://minne.com/category/saleonly/stationery?sort=none&input_method=typing&q=" + x[2])
        })

    };
    printAddress();

}

