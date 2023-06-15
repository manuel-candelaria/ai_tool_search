

  function splitAndDisplay() {
    const inputString = "#video editing\r\n#video generator\r\n#personalized videos";
    let outputArray = splitStringByHash(inputString);


    const inputElement = document.getElementById("originArray");
    inputElement.textContent = inputString;

    const outputElement = document.getElementById("outArray");
    outputElement.textContent = outputArray;

    const sizeElement = document.getElementById("arraySize");
    sizeElement.textContent = outputArray.length;

  }

  function splitStringByHash(inputString) {
    const outputArray = inputString.split("#").filter(item => item.trim() !== "");
    return outputArray;
  }
