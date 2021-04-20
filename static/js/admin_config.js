$('#save-btn1').on('click', function (){
    const body = {
        terms: tinyMCE.get('toc_editor').getContent()
    }
    $.ajax("/api/static-content/1", {
        method: "PATCH",
        contentType: "application/json",
        headers: {
            'Accept-Language': 'fa',
        },
        data: JSON.stringify(body),
    })
})

$('#save-btn2').on('click', function (){
    const body = {
        terms_seller: tinyMCE.get('seller_toc_editor').getContent()
    }
    $.ajax("/api/static-content/1", {
        method: "PATCH",
        contentType: "application/json",
        headers: {
            'Accept-Language': 'fa',
        },
        data: JSON.stringify(body),
    })
})

$('#save-btn3').on('click', function (){
    const body = {
        terms_logistic: tinyMCE.get('logistic_toc_editor').getContent()
    }
    $.ajax("/api/static-content/1", {
        method: "PATCH",
        contentType: "application/json",
        headers: {
            'Accept-Language': 'fa',
        },
        data: JSON.stringify(body),
    })
})

$('#save-btn4').on('click', function (){
    const body = {
        privacy_policy: tinyMCE.get('privacy_editor').getContent()
    }
    $.ajax("/api/static-content/1", {
        method: "PATCH",
        contentType: "application/json",
        headers: {
            'Accept-Language': 'fa',
        },
        data: JSON.stringify(body),
    })
})