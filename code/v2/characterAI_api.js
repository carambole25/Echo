const fs = require("fs");
const CharacterAI = require('node_characterai');
const characterAI = new CharacterAI();

(async() => {
    await characterAI.authenticateAsGuest();
    const characterId = "YntB_ZeqRq2l_aVf2gWDCZl4oBttQzDvhj9cXafWcF8"
    const chat = await characterAI.createOrContinueChat(characterId);

    var data = fs.readFileSync('fichier_transversale_1.txt', {encoding:'utf8', flag:'r'});
    data = String(data);
    console.log(data);
    var response = await chat.sendAndAwaitResponse(data, true);
    response = response.text;
    console.log(response);
    fs.writeFile('fichier_transversale_2.txt', response, (err) => {if (err) throw err;})
})();