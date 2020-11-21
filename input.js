const { exec } = require('child_process')
let ans;
module.exports.input = async (req, res) => {
    try {

        let USDollar = req.body.a, Temperature = req.body.b, FertilizerperHectare = req.body.c,
            Brightness = req.body.d, Yellowness = req.body.e, OilPrice = req.body.f, PriceOfcompitingcrop = req.body.g,
            FiberTenacity = req.body.h, Climate = req.body.i, State = req.body.j, Month = req.body.k;

        const arr = [USDollar , Temperature , FertilizerperHectare , Brightness , Yellowness , OilPrice , PriceOfcompitingcrop , FiberTenacity , Climate , State , Month];

        // console.log(arr);
        // res.status(200).send(arr);
        exec("python predictor.py " + arr.join(' '), (err, stdout, stderr) => {
            if(err) console.error(err)
            ans = stdout.toString();
            console.log("Before" + ans);
            // console.log(2 + stderr.toString())
            res.status(200).send(ans);
        })
        // console.log(3 + req.body);
    }
    catch (err) {
        console.error(err);
    }
}   
