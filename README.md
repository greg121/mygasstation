#mygasstation

this small tool enables you to track the prices of your favourite gas station using Python 2.7.6, [Pydecoder](https://bitbucket.org/xster/pygeocoder/wiki/Home) and [Tanken](http://tanken.t-online.de/)

##Installation

You might have to install used packages if you don't have them already

    apt-get install python-mechanize python-pip
    pip install pygeocoder
    git clone https://github.com/takluyver/Unidecode.git
    python /Unidecode/setup.py install
    

To download mygasstation you can to clone the git repo 

    git clone https://github.com/greg121/mygasstation.git
    python ~/Unidecode/setup.py install

    
##Usage

This is how to use this tool

    python getPrices.py address fuel [limit]
    
* adress can be a city or a full address
* fuel can be Diesel or Super
* limit is optional and is an integer value to limit the output

##Examples

To retrieve the Diesel prices in Frankfurt you simply type into your command line

    python getPrices.py Frankfurt Diesel
    
and the output looks like this

    Shell Frankfurt Am Main Mörfelder Landstraße: 1.349 (Mörfelder Landstraße 16)
    Bp Tankstelle Vural Demir: 1.349 (Siemensstraße 37)
    Aral: 1.329 (Grüneburgweg 67)
    Aral: 1.339 (Hanauer Landstraße 34-40)
    Esso Frankfurt Am Main: 1.329 (Stresemannallee 10)
    Total: 1.329 (Eckenheimer Landstraße 181)
    Shell Station: 1.349 (Friedberger Landstraße 152)
    Aral: 1.349 (Darmstädter Landstraße 304)
    Shell Mörfelder Landstraße: 1.329 (Mörfelder Landstraße 230)
    Aral: 1.329 (Friedberger Landstraße 300)
    Shell Frankfurt Am Main Kennedyallee: 1.329 (Kennedyallee 120)
    Esso: 1.319 (Spessartstraße 22 - 24)
    Esso Hanauer Landstraße: 1.319 (Hanauer Landstraße 178)

To retrieve the Super prices in Darmstadt in Kasinostrasse 60 but you want to limit the output to three gas stations you type

    python getPrices.py "Darmstadt Kasinostrasse 60" Super 3

and the output looks like this

    Tankstelle Darmstadt Kasinostraße: 1.509 (Kasinostraße 60)
    Esso Darmstadt: 1.519 (Kasinostraße 66)
    Jet: 1.509 (Kasinostraße 75A)
