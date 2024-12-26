

social_icons = """

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Social Media Icons</title>
    <style>
        .social-icons {
            display: flex;
            gap: 10px;
        }
        .social-icons .icon-link {
            text-decoration: none;
            font-size: 24px;
        }
        .far.fa-envelope { color: #D44638; } /* Gmail */
        .fab.fa-linkedin-in { color: #0077B5; } /* LinkedIn */
        .fab.fa-github {color: #181717; /* GitHub */}
        .fab.fa-instagram { color: #E4405F; } /* Instagram */
        .fab.fa-twitter { color: #1DA1F2; } /* Twitter */
        .fab.fa-telegram { color: #0088CC; } /* Telegram */
        .fab.fa-discord { color: #7289DA; } /* Discord */
        
    </style>
</head>
<body>

<div class="social-icons">
    <a href="mailto:shekharsharma100001@gmail.com" class="icon-link"><i class="far fa-envelope"></i></a>
    <a href="https://github.com/Shekharsharma100001" class="icon-link" target="_blank"><i class="fab fa-github"></i></a>
    <a href="https://linkedin.com/in/shekhar100001" class="icon-link" target="_blank"><i class="fab fa-linkedin-in"></i></a>
    <a href="https://www.instagram.com/shekharsharma100001/" class="icon-link" target="_blank"><i class="fab fa-instagram"></i></a>
    <a href="https://t.me/shekharsharma100001" class="icon-link" target="_blank"><i class="fab fa-telegram"></i></a>
    <a href="https://discord.com/invite/A5ZpqUPY" class="icon-link" target="_blank"><i class="fab fa-discord"></i></a>
    <a href="https://x.com/Shekhar100001" class="icon-link" target="_blank"><i class="fab fa-twitter"></i></a>

</div>

<script>
    function hideSocialIcons() {
        var socialIcons = document.querySelector('.social-icons');
        socialIcons.style.display = 'none';
    }
</script>

<!-- Font Awesome CDN for icons -->
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css">

</body>
</html>
"""