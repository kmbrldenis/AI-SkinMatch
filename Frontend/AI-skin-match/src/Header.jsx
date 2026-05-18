

function Header () {

    return (
        <header className = "Header">
            <p id = "greeting"> </p>
            <h1 id = "welcome-message">Hello New Skin</h1>
            <nav>
                <ul id = "nav-list">
                    <li> <a href = "#"> Home </a> </li>
                    <li> <a href = "#">About </a></li>
                    <li> <a href = "#"> Contact us </a></li>
                </ul>
            </nav>
        </header>
    )
}

export default Header