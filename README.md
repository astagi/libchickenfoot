libchickenfoot
==============

Come at Atooma stand and try to hack our Chickenfoot Android controlled car with libchickenfoot!

At Atooma stand connect to BOSS network. After that you can see the car moving, or turn on and off lights, emitting sounds..

This library is very simple and you can just look at the source code to see how it works (I'm very busy here to release some documentation and testing suite).

    import chickenfoot

    chickenfoot.set_lights(chickenfoot.ON)
    chickenfoot.beep(1000)
    chickenfoot.move(chickenfoot.FORWARD, 2000)


Enjoy :)