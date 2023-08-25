function sendConnectionRequest(index) {
    if (index < 10) {
        if (document.querySelectorAll(".entity-result__actions button span")[index].innerText !== "Connect") {
            console.log("PASS");
            setTimeout(() => sendConnectionRequest(index + 1), 1000);
        } else {
            setTimeout(() => {
                document.querySelectorAll(".entity-result__actions button")[index].click();
                setTimeout(() => {
                    document.querySelector(".artdeco-modal__actionbar button:nth-child(1)").click();
                    setTimeout(() => {
                        var fname = document.querySelector("#send-invite-modal").innerText.replace('Invite ', '').replace(' to connect', '');
                        var message = "Hey " + fname + ",\n\nHope you're well! I'm Mohammed Zulfiqar, a UX designer & developer with 4 years of experience. I'm on the lookout for new opportunities. Any chance of discussing potential job openings?\n\nCheers,\nZulfiqar";
                        document.querySelector("#custom-message").value = message;
                        setTimeout(() => {
                            document.querySelector(".artdeco-modal__actionbar button:nth-child(2)").click();
                            console.log("Connect");
                            setTimeout(() => sendConnectionRequest(index + 1), 1000);
                        }, 1000);
                    }, 1000);
                }, 1000);
            }, 1000);
        }
    }
}
sendConnectionRequest(0);