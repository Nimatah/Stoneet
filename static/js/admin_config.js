$('#save-btn1').on('click', function (){
    const body = {
        terms: tinyMCE.get('save-btn1').getContent()
    }
    $.ajax("/api/static-content/1", {
        method: "PATCH",
        content_type: "application/json",
        headers: {
            'Accept-Language': 'fa',
        },
        data: JSON.stringify(body),
    })
})

$('#save-btn2').on('click', function (){
    const body = {
        terms_seller: tinyMCE.get('save-btn2').getContent()
    }
    $.ajax("/api/static-content/1", {
        method: "PATCH",
        content_type: "application/json",
        headers: {
            'Accept-Language': 'fa',
        },
        data: JSON.stringify(body),
    })
})

$('#save-btn3').on('click', function (){
    const body = {
        terms_logistic: tinyMCE.get('save-btn3').getContent()
    }
    $.ajax("api/static-content/1", {
        method: "PATCH",
        content_type: "application/json",
        headers: {
            'Accept-Language': 'fa',
        },
        data: JSON.stringify(body),
    })
})

$('#save-btn4').on('click', function (){
    const body = {
        privacy_policy: tinyMCE.get('save-btn4').getContent()
    }
    $.ajax("api/static-content/1", {
        method: "PATCH",
        content_type: "application/json",
        headers: {
            'Accept-Language': 'fa',
        },
        data: JSON.stringify(body),
    })
})