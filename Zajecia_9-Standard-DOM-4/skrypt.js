function AddStyles() {
    document.querySelector("body > header").style.cssText = "float: left; height: auto; width: 95vw; padding: 5px; margin: 25px; \
    border: #A8A8A8 2px solid; border-style: groove; box-shadow: 0px 0px 10px black; \
    background-color:#eff;";

    document.querySelector("body > nav").style.cssText = "margin: 25px; width: 150px; float: left; \
    border: #A8A8A8 2px solid; border-style: groove; box-shadow: 0px 0px 10px black; \
    background-color:#eff;";

    document.querySelector("body > aside").style.cssText = "float: right; margin: 25px; width: 40vw; height: auto; \
    border: #A8A8A8 2px solid; border-style: groove; box-shadow: 0px 0px 10px black; \
    background-color:#eff;";

    document.querySelector("body > main").style.cssText = "float: left; padding: 5px; margin: 25px; width: 50vw; text-align: left; \
    border: #A8A8A8 2px solid; border-style: groove; box-shadow: 0px 0px 10px black; \
    background-color:#eff;";

    document.querySelector("body > footer").style.cssText = "float: left; height: auto; width: 95vw; padding: 5px; margin: 25px; font-weight: 700; \
    border: #A8A8A8 2px solid; border-style: groove; box-shadow: 0px 0px 10px black; \
    background-color: #eff; ";
}

function RemoveStyles() {
    document.querySelector('body > header').style = '';
    document.querySelector('body > nav').style = '';
    document.querySelector('body > aside').style = '';
    document.querySelector('body > main').style = '';
    document.querySelector('body > footer').style = '';
}