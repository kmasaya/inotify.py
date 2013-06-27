inotifypy = ( interval_time=5, filename="inotifypy.log") ->
    get = =>
        $.ajax(
            type: "GET"
            url: filename
            dataType: "text"
            cache: false
            ifModified: true
        ).done( ( data) =>
            console.log( @time)
            if @time < data
                window.location.reload()
        )

    @time = new Date().getTime() / 1000
    setInterval( get, interval_time*1000)
