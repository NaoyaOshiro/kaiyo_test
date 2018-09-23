<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="Pragma" content="no-cache">
        <meta http-equiv="Cache-Control" content="no-cache">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
        <title>Controller</title>

        <!-- load css files -->
        <link rel="stylesheet" href="static/css/bootstrap.min2.css">
    </head>
    <body>
    <center>
        <main>
          <br>
            <h2>Gyro</h2>
            <div id="txt">ここにデータを表示</div>
            <br>
            <br>
            <h2>Slider</h2>
            <div>
              <!-- <input type="range" value="1" min="1" max="100" step="1" oninput="setLed('0', value=this.value)"> -->
              <form oninput="k.value = a.value">
                go_back :
                <output name="k" >0</output><br>
                <input type="range" min="-100" max="100" step="1" id="a" value="0" oninput="setLed(1, this.value)">
                <br>
              </form>
              <form oninput="k.value = a.value">
                spinturn :
                <output name="k" >0</output><br>
                <input type="range" min="-100" max="100" step="1" id="a" value="0" oninput="setLed(2, this.value)">
                <br>
              </form>
              <form oninput="k.value = a.value">
                up_down :
                <output name="k" >0</output><br>
                <input type="range" min="-100" max="100" step="1" id="a" value="0" oninput="setLed(3, this.value)">
                <br>
              </form>

              <!-- <input type="range" class="input-range" value="100" min="0" max="200" data-unit="%"> -->
            </div>
        </div>
        </main>
        <!-- load script files -->
        <script type="text/javascript" src="static/js/caller.js" charset="utf-8"></script>
    </center>
    </body>
</html>
