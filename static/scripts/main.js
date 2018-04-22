var ctx;
var controlsData = {"x": 0, "y" : 0, "redraw": false};
var previewimg = null;
var userInput = {"forward": 	0, 
				  "backward": 	0, 
				  "left":		0, 
				  "right":		0, 
				  "xAxisLeft": 	0, 
				  "xAxisRight": 0,
				  "yAxisLeft": 	0,
				  "yAxisRight": 0,
				  "brightness": 50,
				  "contrast"  : 50,
				  "image_efect":"none",
				  "awb_mode":"off",
				  "exposure_mode":"off" }

function keydownCallback(e)
{
	if (e.keyCode == "W".charCodeAt(0))
	{
		userInput["forward"] = 1;
		console.log('started forward');
	}
	else if (e.keyCode == "S".charCodeAt(0))
	{
		userInput["backward"] = 1;
		console.log('started backward');
	}
	else if(e.keyCode == "A".charCodeAt(0))
	{
		userInput['left'] = 1;
		console.log('started left');
	}
	else if(e.keyCode == "D".charCodeAt(0))
	{
		userInput["right"] = 1;
		console.log('started right');
	}
	else if (e.keyCode == "Q".charCodeAt(0))
	{
		userInput["xAxisLeft"] = 1;
		console.log("started xAxisLeft");
	}
	else if (e.keyCode == "E".charCodeAt(0))
	{
		userInput["xAxisRight"] = 1;
		console.log("started xAxisRight");
	}
	else if (e.keyCode == "Z".charCodeAt(0))
	{
		userInput["yAxisLeft"] = 1;
		console.log("started yAxisLeft");
	}
	else if (e.keyCode == "C".charCodeAt(0))
	{
		userInput["yAxisRight"] = 1;
		console.log("started yAxisRight");
	}
}

function keyupCallback(e)
{
	if (e.keyCode == "W".charCodeAt(0))
	{
		userInput["forward"] = 0;
		console.log('stopped forward');
	}
	else if (e.keyCode == "S".charCodeAt(0))
	{
		userInput["backward"] = 0;
		console.log('stopped backward');
	}
	else if(e.keyCode == "A".charCodeAt(0))
	{
		userInput['left'] = 0;
		console.log('stopped left');
	}
	else if(e.keyCode == "D".charCodeAt(0))
	{
		userInput["right"] = 0;
		console.log('stopped right');
	}
	else if (e.keyCode == "Q".charCodeAt(0))
	{
		userInput["xAxisLeft"] = 0;
		console.log("stopped xAxisLeft");
	}
	else if (e.keyCode == "E".charCodeAt(0))
	{
		userInput["xAxisRight"] = 0;
		console.log("stopped xAxisRight");
	}
	else if (e.keyCode == "Z".charCodeAt(0))
	{
		userInput["yAxisLeft"] = 0;
		console.log("stopped yAxisLeft");
	}
	else if (e.keyCode == "C".charCodeAt(0))
	{
		userInput["yAxisRight"] = 0;
		console.log("stopped yAxisRight");
	}
}


function controlsManager(canvas, context)
{
	if (controlsData["redraw"])
	{
		// draw circle
		/*context.beginPath();
		context.fillStyle = "#f00";
		context.arc(canvas.width * 0.1, canvas.height* 0.9 , 3, 0, 2 * Math.PI);
		context.stroke();
		context.fill();

		// draw cross
		context.fillRect(canvas.width * 0.8, canvas.height * 0.9, 10, 5);
		context.fillRect(canvas.width * 0.8 + 3, canvas.height * 0.9 - 5, 4, 15);

		controlsData["redraw"] = true;
		*/
	}
}
var intervalID = null;

// register all the components
Vue.component('controls-modal', {
	template: '#controlsModal',
	data: function()  {
		return {
		controlsCanvas: null,
		servo_options: ['slow', 'normal', 'fast'],
		servo_selected_option: "normal",
		motor_options: ["slow", "normal", "max"],
		motor_selected_option: "normal",
		yaw_value: 	 0,
		pitch_value: 0,
		image_effects: ["none", "emboss"],
		image_effect: "none",
		f_brightness: 0,
		l_brightness: 0,
		f_switch: false,
		l_switch: false,
		
		}
	},
	mounted: function()
	{
		var controlsCanvas = document.getElementById('controls-canvas');
		controlsData["x"] = controlsCanvas["y"] = 0;
		controlsData["redraw"] = true;
		intervalID		   = setInterval(function () {controlsManager(controlsCanvas, controlsCanvas.getContext('2d'))}, 1000 / 20);
		previewimg = document.getElementById('view');
		previewimg.style.display = 'none';

		// add listeners
		window.addEventListener("keydown", keydownCallback);
		window.addEventListener("keyup", keyupCallback);
		
		
	},
	destroyed: function()
	{
		clearInterval(this.intervalID);
		previewimg.style.display = 'inline';
		window.removeEventListener("keydown", keydownCallback);
		window.removeEventListener("keyup", keyupCallback);
	}
  })
Vue.component('visuals-modal',
{
	template:'#visualsModal',
	data: function()
	{
		return{
			theme_options: ["default", "light"],
			theme: "default"
		}
	},
	mounted: function()
	{

	},
	destroyed: function()
	{

	}
})
Vue.component('audio-modal',
{
	template:'#audioModal',
	data: function()
	{
		return{
			whatToSay: null,
			question: null,
			audio_volume: 0
		}
	},
	mounted: function()
	{

	},
	destroyed: function()
	{

	}
})
Vue.component('options-modal',
{
	template:'#optionsModal',

	data: function()
	{
		return {
			allowLaser:false,
			  allowFlashlight: false,
              allowCOsensor: false,
              allowGoogleMaps: false,
              allowTemperature: false,
			  allowHumilidity: false,
              allowCPUTemp: false,
              allowCpuPercent: false
		}
	},
	mounted: function()
	{

	},
	destroyed: function()
	{

	}
})

var app = new Vue({
	name: 'robot-panel',
	el: '#panel-root',
	data: { title: 'Raspi-Bot',
			socket: null,
			showControls:false,
			showVisuals:false,
			showAudio:false,	
			showFeatures:false,
			showOptions:false,
			moveDetected:false,
			laserOn:  false,
			flashlightOn: false,
			flashlight_on : "flashlight_on",
			flashlight_off : "flashlight_off",
			laser_on : "laser_on",
			laser_off : "laser_off" 
		},
	delimiters: ['[$', '$]'],
	methods: 
	{
		openProcessingPanel: function()
		{
			debugPrint("panel");
		},
		switchFlashlight : function()
		{
			this.socket.emit("flashlight");
		}
		,switchLaser : function()
		{
			this.socket.emit("laser");
		},
		buzz: function()
		{
			this.socket.emit("buzz");
		},
	},
	created: function()
	{
		this.socket = io.connect("http://" + document.domain + ':' + location.port);		

		this.socket.on('data', function(data)
		{
			app.flashlightOn  = data['flashlight']; 
			app.laserOn 	  = data['laser'];
			app.cpuUsage  	  = "Cpu usage: " + data['CPU'] + " %";
			app.temperature  = "temperature: " + data["temperature"] + " C";			
			console.log(data);
		});
	}
});
