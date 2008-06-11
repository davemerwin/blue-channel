/*
 * Site Settings
 *
 * Copyright (c) 2008 Dave Merwin
 * Dependencies: 
 *
 */
$(document).ready(function(){
    
    $('#subNav li ul.subNavMenu')
        .parent()
        .prepend('<a href="" class="subNavToggle">' + '<span class="closeButton">Close</span>' + '<span class="openButton">Open</span></a>');
        
    // Close all submenus
    $('#subNav li > ul.subNavMenu > li').hide();
    // Open menus on the active path
    $('#subNav li.active > ul.subNavMenu > li').show();
    // Make buttons appear opened on active path
    $('#subNav li.active a.subNavToggle span.openButton').hide();
    $('#subNav li.active a.subNavToggle span.closeButton').show();
    // Click event for toggle buttons...
    $('a.subNavToggle').click(function() {
        if ($(this).children('span.openButton:hidden').length > 0) {
            // if open button is hidden, it's already open: no-op
            $(this).siblings('ul.subNavMenu').children('li').slideUp('fast');
            $(this).children('span').toggle();
            return false;
        }
        // Close all lists and set button state to closed
        $('#subNav li > ul.subNavMenu > li').slideUp('fast');
        $('#subNav li > a.subNavToggle > span.openButton').show();
        $('#subNav li > a.subNavToggle > span.closeButton').hide();
        // Open the sibling list that was clicked and set button state to opened
        $(this).siblings('ul.subNavMenu').children('li').slideDown('fast');
        $(this).children('span').toggle();
        return false;
    });
    
    // Sidebar Module Toggle
    $('.moduleToggle a').click(function() {
        $(this).parent().siblings().slideToggle();
        return false;
    });
    
    // Column Toggle
    $('#twoColumns').click(function() {
        // Remove width classes
        $('#sidebar').removeClass('grid_8').children().removeClass('grid_4').removeClass('omega');
        $('#pageContent').removeClass('grid_8');
        $('#sidebar').addClass('grid_4');
        $('#pageContent').addClass('grid_12');
        return false;
    });
    
    $('#threeColumns').click(function() {
        // Remove width classes
        $('#sidebar').removeClass('grid_4');
        $('#pageContent').removeClass('grid_12');
        $('#sidebar').children('div').addClass('grid_4');
        $('#pageContent').addClass('grid_8');
        return false;
    });
    
    // Footer Equal Column Heights
    var columns = $('.highlightBlocks').height();
    $('.highlightBlocks').children('div').height(columns);
});