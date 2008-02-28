/*
 * Site Settings For Site
 *
 * Copyright (c) 2008 Dave Merwin (davemerwin.com)
 *
 */
 $(document).ready(function(){
     $.slideshow(
     	{
     		container : 'slideshow1',
     		loader: 'images/slideshow_loader.gif',
     		linksPosition: 'bottom',
     		linksClass: 'pagelinks',
     		linksSeparator : ' | ',
     		fadeDuration : 400,
     		activeLinkClass: 'activeSlide',
     		nextslideClass: 'nextSlide',
     		prevslideClass: 'prevSlide',
     		captionPosition: 'bottom',
     		captionClass: 'slideCaption',
     		autoplay: 0,
     		images : [
     			{
     				src: 'http://farm2.static.flickr.com/1209/1024865660_d4517d8c5d.jpg',
     				caption: 'On The Way Down'
     			},
     			{
     				src: 'http://farm2.static.flickr.com/1438/1024926078_bec4b00d78.jpg',
     				caption: 'Here I Go'
     			},
     			{
     				src: 'http://farm2.static.flickr.com/1035/1024970720_7dda91aef3.jpg',
     				caption: 'Brave Explorer'
     			},
     			{
     				src: 'http://farm2.static.flickr.com/1396/1023952257_6c61339879.jpg',
     				caption: 'Full Speed Emma'
     			}
     		]
     	}
     );
 });