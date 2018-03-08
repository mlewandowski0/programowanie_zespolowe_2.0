var canvas = document.getElementById('background');
var ctx		 = canvas.getContext('2d');

// function that is called once, that setup and create background colors, cool stuff and anmations
function initBackground()
{
		createBackground();

    // draw some simple animations, cuz why not
    setInterval( function()
    {
       ctx.fillStyle = '#FF0000';
       ctx.fillRect(1000,200,100,100);
       console.log('xdd');

    }, 100);
}

function createBackground()
{
	var my_gradient = ctx.createLinearGradient(0,0,0,170);
	my_gradient.addColorStop(0, '#9c38d0');
	my_gradient.addColorStop(1, '#330065');
	document.querySelector('body').style.backgroundColor = '#330065';

	ctx.fillStyle = my_gradient;
	ctx.fillRect(0,0,canvas.width, canvas.height);
}

// first call that will initialize background
initBackground();

