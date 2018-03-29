# using firefox --> copy --> css selector
# http://data.eastmoney.com/hsgt/top10.html
# ruby builder.rb hgt.yaml http://data.eastmoney.com/hsgt/top10.html

website:
  url: 'ARGV[1]' #'http://hf.273.cn/car/10390340.html'
  encode: 'utf-8'
  retry-delay: '3' #secs
  retry: '3' #times
  max-time: '20' #secs
  #proxy: '116.53.8.105:2386'
  #duan-dian: 'false'
  output: 'file'
  #output: 'stdout' #or 'db'

list:
  leibie:
    from: '.breadcrumb > li:nth-child(2) > a:nth-child(1)'
  images[]:
    from: 'ul.list-unstyled:nth-child(2)'
    img1:
      from[0]: 'li a'
      attr: 'href'
    img2:
      from[1]: 'li a'
      attr: 'href'
    img3:
      from[2]: 'li a'
      attr: 'href'
    img4:
      from[3]: 'li a'
      attr: 'href'
    img5:
      from[4]: 'li a'
      attr: 'href'
    img6:
      from[5]: 'li a'
      attr: 'href'
    img7:
      from[6]: 'li a'
      attr: 'href'
    img8:
      from[7]: 'li a'
      attr: 'href'
    img9:
      from[8]: 'li a'
      attr: 'href'
    img10:
      from[9]: 'li a'
      attr: 'href'
  title:
    from: 'div.panel-smart h2'
  price:
    from: '.price-new'  
  desc:
    from: 'div.col-sm-8:nth-child(2) > div:nth-child(1) > div:nth-child(9)'
  detail1:
    from: '#tab-description'
  detail2[]:
    from: '#tab-description > p:nth-child(1) > strong:nth-child(1) > span:nth-child(1) > span:nth-child(1) > span:nth-child(1)'
    img1:
      from[0]: 'img'
      attr: 'src'
    img2:
      from[1]: 'img'
      attr: 'src'
    img3:
      from[2]: 'img'
      attr: 'src'
    img4:
      from[3]: 'img'
      attr: 'src'
    img5:
      from[4]: 'img'
      attr: 'src'
    img6:
      from[5]: 'img'
      attr: 'src'
    img7:
      from[6]: 'img'
      attr: 'src'
    img8:
      from[7]: 'img'
      attr: 'src'
    img9:
      from[8]: 'img'
      attr: 'src'
    img10:
      from[9]: 'img'
      attr: 'src'
    

