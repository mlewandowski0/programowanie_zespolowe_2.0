Vue.component('processing',
{
	template: "#imgProcessingPanel"
})


var app = new Vue({
	name: 'robot-panel',
	el: '#panel-root',
	data: { title: 'Raspi-Bot',
			showProcessing:false
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
			socket.emit("flashlight");
		}
		,switchLaser : function()
		{
			socket.emit("laser");
		},
		buzz: function()
		{
			socket.emit("buzz");
		},
		openDiagnosticsPanel: function()
		{
			debugPrint("diagnostics");
		},
		openAudioPanel: function()
		{
			debugPrint("audio");
		}
	}
});
