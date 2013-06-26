inotifypy = ( filename="inotifypy.log", interval_time=5) ->
    get = =>
        $.ajax(
            type: "GET"
            url: filename
            dataType: "text"
            cache: false
            ifModified: true
        ).done( ( data) ->
            if @time < data
                window.location.reload()
        )

    time = new Date().getTime() / 1000
    setInterval( get, interval_time*1000)
