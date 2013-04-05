aza.align = function(identifier, type, lineLengths, tolerance, center) {
	var canvas = $(identifier).get(0),
		context = canvas.getContext && canvas.getContext('2d'),
		format, nodes, breaks;
	if (context) {
		context.textBaseline = 'top';
		//context.font = "14px 'times new roman', 'FreeSerif', serif";

		format = formatter(function (str) {
			return context.measureText(str).width;
		});

		nodes = format[type](text);

		breaks = linebreak(nodes, lineLengths, {tolerance: tolerance});

		if (breaks.length !== 0) {
			draw(context, nodes, breaks, lineLengths, center);
		} else {
			context.fillText('Paragraph can not be set with the given tolerance.', 0, 0);
		}
	}
	return [];
}


aza.draw = function(context, nodes, breaks, lineLengths, center) {
	var i = 0, lines = [], point, j, r, lineStart = 0, y = 4, tmp, maxLength = Math.max.apply(null, lineLengths);

	// Iterate through the line breaks, and split the nodes at the
	// correct point.
	for (i = 1; i < breaks.length; i += 1) {
		point = breaks[i].position,
		r = breaks[i].ratio;

		for (var j = lineStart; j < nodes.length; j += 1) {
			// After a line break, we skip any nodes unless they are boxes or forced breaks.
			if (nodes[j].type === 'box' || (nodes[j].type === 'penalty' && nodes[j].penalty === -linebreak.infinity)) {
				lineStart = j;
				break;
			}
		}
		lines.push({ratio: r, nodes: nodes.slice(lineStart, point + 1), position: point});
		lineStart = point;
	}

	lines.forEach(function (line, lineIndex) {
		var x = 0, lineLength = lineIndex < lineLengths.length ? lineLengths[lineIndex] : lineLengths[lineLengths.length - 1];

		if (center) {
			x += (maxLength - lineLength) / 2;

		}

		line.nodes.forEach(function (node, index, array) {
			if (node.type === 'box') {
				context.fillText(node.value, x, y);
				x += node.width;
			} else if (node.type === 'glue') {
				x += node.width + line.ratio * (line.ratio < 0 ? node.shrink : node.stretch);
			} else if (node.type === 'penalty' && node.penalty === 100 && index === array.length - 1) {
                context.fillText('-', x, y);
            }
		});

		y += 21;
	});
}

jQuery(function($) {
	var items = $('p');
	items.each(function(p) {
		aza.align(items[p], 800);
	});
});
/*
jQuery(function ($) {
	function browserTypeset() {
		var original = $('#browser'),
			width = original.width(),
			copy = original.clone(),
			text = copy.text(),
			lines = [],
			ratios = [],
			words = text.split(/\s/),
			position = 0,
			stretchWidth = 0,
			spaceStretch = 0,
			html = [];

		$('body').append(copy);

		// This piece of code calculates the positions of the line breaks added
		// by the browser by adding an invisible wrapper element to each word
		// and checking when its y-position changes.
		words.forEach(function (word, index) {
            var html = words.slice(0, index),
				currentPosition = 0;

            html.push('<span>' + word + '</span>');
            Array.prototype.push.apply(html, words.slice(index + 1, words.length));

			copy.html(html.join(' '));

			currentPosition = copy.find('span').position().top;

			if (currentPosition != position) {
				lines.push([]);
				position = currentPosition;
			}

			lines[lines.length - 1].push(word);
		});

		lines = lines.map(function (line) {
			return line.join(' ');
		});


		// We measure the width if the text is not justified and only a
		// single line (i.e. the optimal line length.)
		copy.empty();
		copy.css({width: 'auto', display: 'inline', textAlign: 'left'});

		// This works under the assumption that a space is 1/3 of an em, and
		// the stretch value is 1/6. Although the actual browser value may be
		// different, the assumption is valid as it is only used to compare
		// to the ratios calculated earlier.
		stretchWidth = copy.html('&nbsp;').width() / 2;

		lines.forEach(function (line, index) {
			// This conditional is to ensure we don't calculate the ratio
			// for the last line as it is not justified.
			if (index !== lines.length - 1) {
				copy.text(line);
				ratios.push((width - copy.width()) / ((line.split(/\s/).length - 1) * stretchWidth));
			} else {
				ratios.push(0);
			}
		});

		copy.remove();


		html.push('<ul>');
		ratios.forEach(function (ratio) {
			html.push('<li>');
			html.push(ratio.toFixed(3));
			html.push('</li>');
		});
		html.push('</ul>');

		$('#browser').parent().append(html.join(''));
	}

	$('#browser').text(text);
	browserTypeset();
});
*/