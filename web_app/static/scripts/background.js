var canvas = document.getElementById('background');
var ctx		 = canvas.getContext('2d');

// function that is called once, that setup and create background colors, cool stuff and anmations
function initBackground()
{
		createBackground();

    // draw some simple animations, cuz why not

}

function animation()
{
	console.log('xddd');

	ctx.fillStyle = '#ff0000';
	ctx.arc(600,500,100,0,2 * Math.PI);
}


function createBackground()
{
	var my_gradient = ctx.createRadialGradient(75,50,5,90,60,100);
	my_gradient.addColorStop(0, '#233237');
	my_gradient.addColorStop(1, '#18121E');
	document.querySelector('body').style.backgroundColor = '#18121E';

	ctx.fillStyle = my_gradient;
	ctx.fillRect(0,0,canvas.width, canvas.height);
}

// first call that will initialize background
initBackground();


setInterval(animation, 100);