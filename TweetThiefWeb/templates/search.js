// import {PythonShell} from 'python-shell';
// import { PythonShell } from 'python-shell';
import { PythonShell } from 'python-shell';

console.log("hello");
function searchUsername() { 
    let input = (document.getElementById("searchbar").value).toLowerCase;
    let userUrl = "https://api.twitter.com/2/users/by/username/" + input;
    console.log(userUrl);
                    
    PythonShell.run(
        'fetch.py',
        null,
        function(err) {
            if (err) throw err;
            console.log('finished');
        }
    );
}

let searchBarButton = document.getElementById("searchbutton");
searchBarButton.addEventListener('click', event => {  
    event.preventDefault();      
    searchUsername();
} 
);
