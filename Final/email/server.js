const express = require('express');
const app = express();

app.get('/', (req, res) => {
  res.sendFile(process.cwd()+"/email.html");
});

app.get('/sendemail/:addr', (req, res) => {
    let address = req.params.addr;
    var exec = require('child_process').exec;

    exec('python3 notify.py ' + address,
        function (error, stdout, stderr) {
            console.log('stdout: ' + stdout);
            console.log('stderr: ' + stderr);
            if (error !== null) {
                 console.log('exec error: ' + error);
            }
        });
    let txt = '{"check" : "successful"}'
    res.send(JSON.parse(txt))
});

// Listen to the App Engine-specified port, or 8080 otherwise
const PORT = process.env.PORT || 8080;
app.listen(PORT, () => {
  console.log(`Server listening on port ${PORT}...`);
});