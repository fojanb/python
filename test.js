function compose(array, x) {
    let isConstraint = (x <= 1000 && x >= -1000) && (array.length <= 1000 && array.length > 0);
    let flag = 0;
    array.forEach(fn => {
        if (fn.length > 1 || fn.length == 0) {
            flag++;
        }
    });
    if (isConstraint && !flag) {
        let n = array.length - 1, final_result, temp_result;
        while (n != 1) {
            temp_result = array[n](x);
            n = n - 1;
            final_result = array[n](temp_result);
        }
        console.log(array[0](final_result));
    } else {
        if (array.length == 0) {
            console.log(x)
        } else {
            console.log("Your inputs did not meet the .");
        }
    }
}
compose([x=>x*100], 20)
