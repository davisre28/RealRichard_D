var $tooltip = $('#fullsize');

$('img').on('mouseenter', function() {
    var img = this,
        $img = $(img),
        offset = $img.offset();
    
    $tooltip
    .css({
        'top': offset.top,
        'left': offset.left
    })
    .append($img.clone())
    .removeClass('hidden');
});

$tooltip.on('mouseleave', function() {
    $tooltip.empty().addClass('hidden');
});
