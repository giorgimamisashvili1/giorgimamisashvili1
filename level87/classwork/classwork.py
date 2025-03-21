#M1
 #Promise არის JavaScript-ის ობიექტი. იგი წარმოადგენს „მომავალ შედეგს“, რომელიც შეიძლება იყოს წარმატებული (fulfilled), ან შეცდომა (rejected).
let promise = new Promise(function(resolve, reject) {
  let success = true;

  if (success) {
    resolve("Success!");  // Promise-ი წარმატებით შესრულდა
  } else {
    reject("Error!");  // Promise-ი ვერ შესრულდა
  }
});

promise
  .then(function(result) {
    console.log(result);  // "Success!" თუ resolve მოხდა
  })
  .catch(function(error) {
    console.log(error);  // "Error!" თუ reject მოხდა
  });

#N2
  let fetchData = new Promise(function(resolve, reject) {
  // სიმულირება, რომ ინფორმაცია იღება სერვერიდან
  setTimeout(function() {
    let success = true;  // თუ `success` შეცვლით false-ზე, იქნება "rejected"

    if (success) {
      resolve("მონაცემები წარმატებით მიიღეს სერვერიდან!");
    } else {
      reject("შეცდომა მოხდა მონაცემების მიღებისას!");
    }
  }, 2000);  // 2 წამი (2000ms) სიმულაციისთვის
});

fetchData
  .then(function(result) {
    console.log(result);  // აქ მიიღებთ წარმატებულ ინფორმაციას
  })
  .catch(function(error) {
    console.log(error);  // თუ something went wrong
  });

#N3 

 let fetchData = new Promise(function(resolve, reject) {
  // სიმულირება, რომ ინფორმაცია იღება სერვერიდან
  setTimeout(function() {
    let success = false;  // შეცდომა შევქმნით, რომ Promise-ი დამთავრდეს როგორც rejected

    if (success) {
      resolve("მონაცემები წარმატებით მიღებულია!");
    } else {
      reject("შეცდომა მოხდა მონაცემების მიღებისას!");
    }
  }, 2000);  // 2 წამი (2000ms) სიმულაციისთვის
});

fetchData
  .then(function(result) {
    console.log(result);  // ეს აღარ ამუშავდა, რადგან Promise-ი rejected იყო
  })
  .catch(function(error) {
    console.log(error);  // "შეცდომა მოხდა მონაცემების მიღებისას!" დაიბეჭდება
  });

#N4
  let fetchData = new Promise(function(resolve, reject) {
  // სიმულირება, რომ მონაცემები იძენება სერვერიდან
  setTimeout(function() {
    let isSuccess = Math.random() > 0.5;  // შემთხვევითი პირობა, რათა იყოს 50%-იანი შანსი წარმატებისა ან შეცდომის

    if (isSuccess) {
      resolve("მონაცემები წარმატებით მიიღეს!");
    } else {
      reject("შეცდომა მოხდა მონაცემების მიღებისას!");
    }
  }, 2000);  // 2 წამი (2000ms) სიმულაციისთვის
});

fetchData
  .then(function(result) {
    console.log(result);  // წარმატების შემთხვევაში
  })
  .catch(function(error) {
    console.log(error);  // შეცდომის შემთხვევაში
  });