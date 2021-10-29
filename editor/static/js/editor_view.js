let editor;

ClassicEditor
    .create(document.querySelector('#editor'))
    .then(newEditor => {
        editor = newEditor;
    })
    .catch(error => {
        console.error(error);
    });

// Assuming there is a <button id="submit">Submit</button> in your application.
document.querySelector('h1').addEventListener('click', () => {
    const editorData = editor.getData();

    console.log(typeof (editorData));
});


document.querySelector("#submit1").addEventListener("click", event => {
    const editorData = editor.getData();
    document.querySelector("#content1").value = editorData;
});
