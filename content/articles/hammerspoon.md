+++
title = "The quest to get a mac to do exactly what I want"
description = "It all started because I use a weird keyboard. When I don't have this"
date = 2017-06-23T07:29:12Z
[taxonomies]
tags = ["computers"]
+++

keyboard plugged in, I want my laptop keyboard map to use dvorak, but
since my keyboard is dvorak in hardware, when it's plugged in, the
laptop's keyboard map needs to be switched to qwerty otherwise I get a
kind of "double dvorak" and everything goes down an extremely strange
rabbit hole. Now normally it wouldn't be that much of a hassle to just
change it when I'm plugging or unplugging my keyboard, but I found
myself in a situation when I kept having to take my laptop to one or
other meeting, meaning that I would be plugging and unplugging the
keyboard and flipping the setting multiple times a day.

As a nerd, this grates. The computer should just know that if I have
that keyboard plugged in I want the keyboard mapping to be qwerty and
otherwise I want it to be dvorak. Happily, this is where [hammerspoon][3]
comes in. Hammerspoon is a framework that allows you to program all
kinds of little customizations for mac. Here's how you do the keyboard
tweak I wanted:

```lua
-- Watch for planck keyboard add/remove and set the keyboard layout
--appropriately
function usbDeviceCallback(data)
    -- Skip internal memory card as it spams an event on suspend/resume
    if (data["productName"] ~= "Internal Memory Card Reader") then
        hs.alert(data["productName"] .. " " .. data["eventType"])
    end

    if (data["productName"] == "Planck") then
        if (data["eventType"] == "added") then
            --when we add the planck, change the hardware layout to
            --dvorak and turn the OS key layout to qwerty
            hs.keycodes.setLayout("U.S.")
        elseif (data["eventType"] == "removed") then
            --when we remove the planck, change the hardware layout to
            --qwerty. It's up to the OS to give me dvorak
            hs.keycodes.setLayout("Dvorak")
        end
    end
end
usbWatcher = hs.usb.watcher.new(usbDeviceCallback)
usbWatcher:start()
```

...but of course this turned out to be a gateway drug for all kinds of
further customizations. How about a thing that starts the annoying
WeWork printer client thing whenever I'm at WeWork? (Yup. Done).
Automatically tweaks my brightness taking into account my battery
percentage and the ambient brightness of the room I'm in? (Yup. Easy
peasy). Set a default layout of windows whenever I plug my laptop into
an external monitor? (Sure) I've now also got it so I can do almost all
window movement and resizing via the keyboard.

Any case, my full config is unavailable right now but I'll try to get it back
when my personal mac is brought back to life. Feel free to take from it anything
that's usable. The grid resizing thing has a minor bug that I've not
been annoyed enough to fix yet, where on certain sizes of monitor it
doesn't realise your window is on at the bottom, so you need to move it
up to resize. Other than that it's tickety-boo. I highly recommend
checking hammerspoon out if you can code a little and want to tweak a
Mac to behave exactly the way you want.

[3]: http://www.hammerspoon.org/
[4]: https://www.uncarved.com/static/init.lua.txt
