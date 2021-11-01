let editor;
let form = document.querySelector('#form');

ClassicEditor
    .create(document.querySelector('#editor'))
    .then(newEditor => {
        editor = newEditor;
    })
    .catch(error => {
        console.error(error);
    });

// Assuming there is a <button id="submit">Submit</button> in your application.
form.addEventListener('submit', (event) => {
    const editorData = editor.getData();
    document.querySelector('#content').value = editorData;
    //form.submit();
    
});


// document.querySelector("#submit1").addEventListener("click", event => {
//     const editorData = editor.getData();
//     document.querySelector("#content1").value = editorData;
// });