import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
import csv

#sender_email = "psantiago@pacandev.com"
#password = 'wijwsuyuucahdwep'
sender_email = "ops@pacandev.com"
password = "ezxgkrrppbjdaasf"


# Lista de destinatarios
lista = []
with open('plantilla html.txt') as f:
    for line in f:
        lista = [elt.strip() for elt in line.split(',')]

# Crear un objeto MIMEMultipart para el mensaje
message = MIMEMultipart("alternative")
message["Subject"] = "Optimiza tu Eficiencia Empresarial con Nuestros Servicios de Automatización RPA - PacanDev"
message["From"] = sender_email

# Agregar contenido HTML con una imagen
html = """
<!DOCTYPE html>
<!-- saved from url=(0076)https://us21.campaign-archive.com/?u=e2362628fe7166cce029a58b4&id=29c339ed67 -->
<html xmlns:fb="http://www.facebook.com/2008/fbml" xmlns:og="http://opengraph.org/schema/" data-lt-installed="true"><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        
<meta property="og:title" content="Optimiza tu Eficiencia Empresarial con Nuestros Servicios de Automatización RPA">
<meta property="fb:page_id" content="43929265776">
<meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1">
<meta name="referrer" content="origin">
    </head>
<!--[if gte mso 15]>
<xml>
<o:OfficeDocumentSettings>
<o:AllowPNG/>
<o:PixelsPerInch>96</o:PixelsPerInch>
</o:OfficeDocumentSettings>
</xml>
<![endif]-->

<meta http-equiv="X-UA-Compatible" content="IE=edge">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Optimiza tu Eficiencia Empresarial con Nuestros Servicios de Automatización RPA</title>
<style>          img{-ms-interpolation-mode:bicubic;} 
          table, td{mso-table-lspace:0pt; mso-table-rspace:0pt;} 
          .mceStandardButton, .mceStandardButton td, .mceStandardButton td a{mso-hide:all !important;} 
          p, a, li, td, blockquote{mso-line-height-rule:exactly;} 
          p, a, li, td, body, table, blockquote{-ms-text-size-adjust:100%; -webkit-text-size-adjust:100%;} 
          @media only screen and (max-width: 480px){
            body, table, td, p, a, li, blockquote{-webkit-text-size-adjust:none !important;} 
          }
          .mcnPreviewText{display: none !important;} 
          .bodyCell{margin:0 auto; padding:0; width:100%;}
          .ExternalClass, .ExternalClass p, .ExternalClass td, .ExternalClass div, .ExternalClass span, .ExternalClass font{line-height:100%;} 
          .ReadMsgBody{width:100%;} .ExternalClass{width:100%;} 
          a[x-apple-data-detectors]{color:inherit !important; text-decoration:none !important; font-size:inherit !important; font-family:inherit !important; font-weight:inherit !important; line-height:inherit !important;} 
            body{height:100%; margin:0; padding:0; width:100%; background: #ffffff;}
            p{margin:0; padding:0;} 
            table{border-collapse:collapse;} 
            td, p, a{word-break:break-word;} 
            h1, h2, h3, h4, h5, h6{display:block; margin:0; padding:0;} 
            img, a img{border:0; height:auto; outline:none; text-decoration:none;} 
            a[href^="tel"], a[href^="sms"]{color:inherit; cursor:default; text-decoration:none;} 
            li p {margin: 0 !important;}
            .ProseMirror a {
                pointer-events: none;
            }
            @media only screen and (max-width: 480px){
                body{width:100% !important; min-width:100% !important; } 
                body.mobile-native {
                    -webkit-user-select: none; user-select: none; transition: transform 0.2s ease-in; transform-origin: top center;
                }
                body.mobile-native.selection-allowed a, body.mobile-native.selection-allowed .ProseMirror {
                    user-select: auto;
                    -webkit-user-select: auto;
                }
                colgroup{display: none;}
                img{height: auto !important;}
                .mceWidthContainer{max-width: 660px !important;}
                .mceColumn{display: block !important; width: 100% !important;}
                .mceColumn-forceSpan{display: table-cell !important; width: auto !important;}
                .mceBlockContainer{padding-right:16px !important; padding-left:16px !important;} 
                .mceBlockContainerE2E{padding-right:0px; padding-left:0px;} 
                .mceSpacing-24{padding-right:16px !important; padding-left:16px !important;}
                .mceFooterSection .mceText, .mceFooterSection .mceText p{font-size: 16px !important; line-height: 140% !important;}
                .mceText, .mceText p{font-size: 16px !important; line-height: 140% !important;}
                h1{font-size: 30px !important; line-height: 120% !important;}
                h2{font-size: 26px !important; line-height: 120% !important;}
                h3{font-size: 20px !important; line-height: 125% !important;}
                h4{font-size: 18px !important; line-height: 125% !important;}
            }
            @media only screen and (max-width: 640px){
                .mceClusterLayout td{padding: 4px !important;} 
            }
            div[contenteditable="true"] {outline: 0;}
            .ProseMirror .empty-node, .ProseMirror:empty {position: relative;}
            .ProseMirror .empty-node::before, .ProseMirror:empty::before {
                position: absolute;
                left: 0;
                right: 0;
                color: rgba(0,0,0,0.2);
                cursor: text;
            }
            .ProseMirror .empty-node:hover::before, .ProseMirror:empty:hover::before {
                color: rgba(0,0,0,0.3);
            }
            .ProseMirror h1.empty-node:only-child::before,
            .ProseMirror h2.empty-node:only-child::before,
            .ProseMirror h3.empty-node:only-child::before,
            .ProseMirror h4.empty-node:only-child::before {
                content: 'Heading';
            }
            .ProseMirror p.empty-node:only-child::before, .ProseMirror:empty::before {
                content: 'Start typing...';
            }
            a .ProseMirror p.empty-node::before, a .ProseMirror:empty::before {
                content: '';
            }
            .mceText, .ProseMirror {
                white-space: pre-wrap;
            }
body, #bodyTable { background-color: rgb(244, 244, 244); }.mceText, .mceLabel { font-family: "Helvetica Neue", Helvetica, Arial, Verdana, sans-serif; }.mceText, .mceLabel { color: rgb(0, 0, 0); }.mceText p { margin-bottom: 0px; }.mceText ul { margin-bottom: 0px; }.mceText label { margin-bottom: 0px; }.mceText input { margin-bottom: 0px; }.mceSpacing-12 .mceInput + .mceErrorMessage { margin-top: -6px; }.mceText p { margin-bottom: 0px; }.mceText ul { margin-bottom: 0px; }.mceText label { margin-bottom: 0px; }.mceText input { margin-bottom: 0px; }.mceSpacing-24 .mceInput + .mceErrorMessage { margin-top: -12px; }.mceInput { background-color: transparent; border: 2px solid rgb(208, 208, 208); width: 60%; color: rgb(77, 77, 77); display: block; }.mceInput[type="radio"], .mceInput[type="checkbox"] { float: left; margin-right: 12px; display: inline; width: auto !important; }.mceLabel > .mceInput { margin-bottom: 0px; margin-top: 2px; }.mceLabel { display: block; }.mceText p { color: rgb(0, 0, 0); font-family: "Helvetica Neue", Helvetica, Arial, Verdana, sans-serif; font-size: 16px; font-weight: normal; line-height: 1.5; text-align: center; letter-spacing: 0px; direction: ltr; }.mceText a { color: rgb(0, 0, 0); font-style: normal; font-weight: normal; text-decoration: underline; direction: ltr; }
@media only screen and (max-width: 480px) {
            .mceText p { font-size: 16px !important; line-height: 1.5 !important; }
          }
@media only screen and (max-width: 480px) {
            .mceBlockContainer { padding-left: 16px !important; padding-right: 16px !important; }
          }
#dataBlockId-9 p, #dataBlockId-9 h1, #dataBlockId-9 h2, #dataBlockId-9 h3, #dataBlockId-9 h4, #dataBlockId-9 ul { text-align: center; }</style>                 <link rel="stylesheet" href="./Optimiza tu Eficiencia Empresarial con Nuestros Servicios de Automatización RPA_files/archivebar-desktop.css" mc:nocompile="">  
<script>!function(){function o(n,i){if(n&&i)for(var r in i)i.hasOwnProperty(r)&&(void 0===n[r]?n[r]=i[r]:n[r].constructor===Object&&i[r].constructor===Object?o(n[r],i[r]):n[r]=i[r])}try{var n=decodeURIComponent("%7B%0A%22ResourceTiming%22%3A%7B%0A%22comment%22%3A%20%22Clear%20RT%20Buffer%20on%20mPulse%20beacon%22%2C%0A%22clearOnBeacon%22%3A%20true%0A%7D%2C%0A%22AutoXHR%22%3A%7B%0A%22comment%22%3A%20%22Monitor%20XHRs%20requested%20using%20FETCH%22%2C%0A%22monitorFetch%22%3A%20true%2C%0A%22comment%22%3A%20%22Start%20Monitoring%20SPAs%20from%20Click%22%2C%0A%22spaStartFromClick%22%3A%20true%0A%7D%2C%0A%22PageParams%22%3A%7B%0A%22comment%22%3A%20%22Monitor%20all%20SPA%20XHRs%22%2C%0A%22spaXhr%22%3A%20%22all%22%0A%7D%0A%7D");if(n.length>0&&window.JSON&&"function"==typeof window.JSON.parse){var i=JSON.parse(n);void 0!==window.BOOMR_config?o(window.BOOMR_config,i):window.BOOMR_config=i}}catch(r){window.console&&"function"==typeof window.console.error&&console.error("mPulse: Could not parse configuration",r)}}();</script>

        
<!---->
<!--[if !gte mso 9]><!----><span class="mcnPreviewText" style="display:none; font-size:0px; line-height:0px; max-height:0px; max-width:0px; opacity:0; overflow:hidden; visibility:hidden; mso-hide:all;">¡No te pierdas esta oportunidad de mejorar tus operaciones empresariales con PacanDev!</span><!--<![endif]-->
<!---->
<center>
<table border="0" cellpadding="0" cellspacing="0" height="100%" width="100%" id="bodyTable" style="background-color: rgb(244, 244, 244);">
<tbody><tr>
<td class="bodyCell" align="center" valign="top">
<table id="root" border="0" cellpadding="0" cellspacing="0" width="100%"><tbody data-block-id="13" class="mceWrapper"><tr><td align="center" valign="top" class="mceWrapperOuter"><!--[if (gte mso 9)|(IE)]><table align="center" border="0" cellspacing="0" cellpadding="0" width="660" style="width:660px;"><tr><td><![endif]--><table border="0" cellpadding="0" cellspacing="0" width="100%" style="max-width:660px" role="presentation"><tbody><tr><td style="background-color:#ffffff;background-position:center;background-repeat:no-repeat;background-size:cover" class="mceWrapperInner" valign="top"><table align="center" border="0" cellpadding="0" cellspacing="0" width="100%" role="presentation" data-block-id="12"><tbody><tr class="mceRow"><td style="background-position:center;background-repeat:no-repeat;background-size:cover" valign="top"><table border="0" cellpadding="0" cellspacing="0" width="100%" role="presentation"><tbody><tr><td style="padding-top:0;padding-bottom:0" class="mceColumn" data-block-id="-14" valign="top" colspan="12" width="100%"><table border="0" cellpadding="0" cellspacing="0" width="100%" role="presentation"><tbody><tr><td style="background-color:#6b9d51;padding-top:0;padding-bottom:0;padding-right:0;padding-left:0" class="mceBlockContainer" valign="top"><table border="0" cellpadding="0" cellspacing="0" width="100%" style="background-color:#6b9d51" role="presentation" data-block-id="15"><tbody><tr><td style="min-width:100%;border-top:20px solid transparent" valign="top"></td></tr></tbody></table></td></tr>
<tbody><tr class="mceRow"><td style="background-position:center;background-repeat:no-repeat;background-size:cover" valign="top"><table border="0" cellpadding="0" cellspacing="0" width="100%" role="presentation"><tbody><tr><td class="mceColumn" data-block-id="-15" valign="top" colspan="12" width="100%"><table border="0" cellpadding="0" cellspacing="0" width="100%" role="presentation"><tbody><tr><td align="center" valign="top"><table align="center" border="0" cellpadding="0" cellspacing="0" width="100%" role="presentation" data-block-id="-5"><tbody><tr class="mceRow"><td style="background-position:center;background-repeat:no-repeat;background-size:cover" valign="top"><table border="0" cellpadding="0" cellspacing="0" width="100%" role="presentation"><tbody><tr><td class="mceColumn" data-block-id="-21" valign="top" colspan="12" width="100%"><table border="0" cellpadding="0" cellspacing="0" width="100%" role="presentation"><tbody><tr><td valign="top"><table align="center" border="0" cellpadding="0" cellspacing="0" width="100%" role="presentation" data-block-id="22"><tbody><tr class="mceRow"><td style="background-position:center;background-repeat:no-repeat;background-size:cover;padding-top:0px;padding-bottom:0px" valign="top"><table border="0" cellpadding="0" cellspacing="24" width="100%" style="table-layout:fixed" role="presentation"><colgroup><col span="1" width="8.333333333333332%"><col span="1" width="8.333333333333332%"><col span="1" width="8.333333333333332%"><col span="1" width="8.333333333333332%"><col span="1" width="8.333333333333332%"><col span="1" width="8.333333333333332%"><col span="1" width="8.333333333333332%"><col span="1" width="8.333333333333332%"><col span="1" width="8.333333333333332%"><col span="1" width="8.333333333333332%"><col span="1" width="8.333333333333332%"><col span="1" width="8.333333333333332%"></colgroup><tbody><tr><td style="padding-top:0;padding-bottom:0" class="mceColumn" data-block-id="19" valign="top" colspan="4" width="33.33333333333333%"><table border="0" cellpadding="0" cellspacing="0" width="100%" role="presentation"><tbody><tr><td style="padding-top:12px;padding-bottom:12px;padding-right:24px;padding-left:24px" class="mceBlockContainer" align="left" valign="top"><img data-block-id="23" width="77.40640809443508" height="auto" style="width:77.40640809443508px;height:auto;max-width:100%;display:block" alt="Logotipo" src="cid:Mailtrapimage" class=""></td></tr></tbody></table></td><td style="padding-top:0;padding-bottom:0;margin-bottom:24px" class="mceColumn" data-block-id="21" valign="top" colspan="8" width="66.66666666666666%"><table border="0" cellpadding="0" cellspacing="0" width="100%" role="presentation"><tbody><tr><td style="padding-top:12px;padding-bottom:12px;padding-right:24px;padding-left:24px" class="mceBlockContainer" valign="top"><div data-block-id="24" class="mceText" id="dataBlockId-24" style="width:100%"><p style="text-align: right;" class="last-child">Noviembre 2023</p></div></td></tr></tbody></table></td></tr></tbody></table></td></tr></tbody></table></td></tr></tbody></table></td></tr></tbody></table></td></tr></tbody></table></td></tr></tbody></table></td></tr></tbody></table></td></tr></tbody></table></td></tr><tr><td style="background-color:#f4f3f3;padding-top:12px;padding-bottom:12px;padding-right:0;padding-left:0" class="mceLayoutContainer" valign="top"><table align="center" border="0" cellpadding="0" cellspacing="0" width="100%" role="presentation" data-block-id="25" id="section_1c9161d6decb2cae679df76786ab3292" class="mceLayout"><tbody><tr class="mceRow"><td style="background-position:center;background-repeat:no-repeat;background-size:cover" valign="top"><table border="0" cellpadding="0" cellspacing="0" width="100%" role="presentation"><tbody><tr><td class="mceColumn" data-block-id="-16" valign="top" colspan="12" width="100%"><table border="0" cellpadding="0" cellspacing="0" width="100%" role="presentation"><tbody><tr><td align="center" valign="top"><table align="center" border="0" cellpadding="0" cellspacing="0" width="100%" role="presentation" data-block-id="-7"><tbody><tr class="mceRow"><td style="background-position:center;background-repeat:no-repeat;background-size:cover" valign="top"><table border="0" cellpadding="0" cellspacing="0" width="100%" role="presentation"><tbody><tr><td class="mceColumn" data-block-id="-22" valign="top" colspan="12" width="100%"><table border="0" cellpadding="0" cellspacing="0" width="100%" role="presentation"><tbody><tr><td valign="top"><table align="center" border="0" cellpadding="0" cellspacing="0" width="100%" role="presentation" data-block-id="30"><tbody><tr class="mceRow"><td style="background-position:center;background-repeat:no-repeat;background-size:cover;padding-top:0px;padding-bottom:0px" valign="top"><table border="0" cellpadding="0" cellspacing="24" width="100%" style="table-layout:fixed" role="presentation"><colgroup><col span="1" width="8.333333333333332%"><col span="1" width="8.333333333333332%"><col span="1" width="8.333333333333332%"><col span="1" width="8.333333333333332%"><col span="1" width="8.333333333333332%"><col span="1" width="8.333333333333332%"><col span="1" width="8.333333333333332%"><col span="1" width="8.333333333333332%"><col span="1" width="8.333333333333332%"><col span="1" width="8.333333333333332%"><col span="1" width="8.333333333333332%"><col span="1" width="8.333333333333332%"></colgroup><tbody><tr><td style="padding-top:0;padding-bottom:0" class="mceColumn" data-block-id="27" valign="top" colspan="8" width="66.66666666666666%"><table border="0" cellpadding="0" cellspacing="0" width="100%" role="presentation"><tbody><tr><td style="padding-top:12px;padding-bottom:12px;padding-right:24px;padding-left:24px" class="mceBlockContainer" valign="top"><div data-block-id="33" class="mceText" id="dataBlockId-33" style="width:100%"><p style="text-align: left;" class="last-child"><strong><span style="font-size: 23px">¡Novedad emocionante! Pacandev se adentra en el mundo de la Automatización de Procesos Robóticos (RPA)</span></strong></p></div></td></tr><tr><td style="padding-top:12px;padding-bottom:12px;padding-right:24px;padding-left:24px" class="mceBlockContainer" valign="top"><div data-block-id="32" class="mceText" id="dataBlockId-32" style="width:100%"><p style="text-align: left;" class="last-child">Estamos emocionados de compartir una emocionante novedad con todos ustedes. En Pacandev, siempre estamos buscando maneras de mejorar y optimizar la forma en que hacemos las cosas, y hoy queremos presentarles una nueva adición a nuestros servicios: Automatización de Procesos Robóticos (RPA).</p></div></td></tr></tbody></table></td><td style="padding-top:0;padding-bottom:0;margin-bottom:24px" class="mceColumn" data-block-id="29" valign="top" colspan="4" width="33.33333333333333%"><table border="0" cellpadding="0" cellspacing="0" width="100%" role="presentation"><tbody><tr><td style="padding-top:74px;padding-bottom:12px;padding-right:0;padding-left:0" class="mceBlockContainerE2E" align="full" valign="top"><img data-block-id="64" width="660" height="auto" style="width:660px;height:auto;max-width:100%;display:block" alt="" src="cid:Mailtrapimage2" role="presentation" class="imageDropZone"></td></tr></tbody></table></td></tr></tbody></table></td></tr></tbody></table></td></tr></tbody></table></td></tr></tbody></table></td></tr></tbody></table></td></tr></tbody></table></td></tr></tbody></table></td></tr></tbody></table></td></tr><tr><td style="background-color:#9bce76;padding-top:12px;padding-bottom:12px;padding-right:0;padding-left:0" class="mceLayoutContainer" valign="top"><table align="center" border="0" cellpadding="0" cellspacing="0" width="100%" role="presentation" data-block-id="34" id="section_ded1850c7702f9269362a02174cc104d" class="mceLayout"><tbody><tr class="mceRow"><td style="background-position:center;background-repeat:no-repeat;background-size:cover" valign="top"><table border="0" cellpadding="0" cellspacing="0" width="100%" role="presentation"><tbody><tr><td class="mceColumn" data-block-id="-17" valign="top" colspan="12" width="100%"><table border="0" cellpadding="0" cellspacing="0" width="100%" role="presentation"><tbody><tr><td align="center" valign="top"><table align="center" border="0" cellpadding="0" cellspacing="0" width="100%" role="presentation" data-block-id="-9"><tbody><tr class="mceRow"><td style="background-position:center;background-repeat:no-repeat;background-size:cover" valign="top"><table border="0" cellpadding="0" cellspacing="0" width="100%" role="presentation"><tbody><tr><td class="mceColumn" data-block-id="-23" valign="top" colspan="12" width="100%"><table border="0" cellpadding="0" cellspacing="0" width="100%" role="presentation"><tbody><tr><td valign="top"><table align="center" border="0" cellpadding="0" cellspacing="0" width="100%" role="presentation" data-block-id="39"><tbody><tr class="mceRow"><td style="background-position:center;background-repeat:no-repeat;background-size:cover;padding-top:0px;padding-bottom:0px" valign="top"><table border="0" cellpadding="0" cellspacing="24" width="100%" style="table-layout:fixed" role="presentation"><colgroup><col span="1" width="8.333333333333332%"><col span="1" width="8.333333333333332%"><col span="1" width="8.333333333333332%"><col span="1" width="8.333333333333332%"><col span="1" width="8.333333333333332%"><col span="1" width="8.333333333333332%"><col span="1" width="8.333333333333332%"><col span="1" width="8.333333333333332%"><col span="1" width="8.333333333333332%"><col span="1" width="8.333333333333332%"><col span="1" width="8.333333333333332%"><col span="1" width="8.333333333333332%"></colgroup><tbody><tr><td style="padding-top:0;padding-bottom:0" class="mceColumn" data-block-id="36" valign="top" colspan="6" width="50%"><table border="0" cellpadding="0" cellspacing="0" width="100%" role="presentation"><tbody><tr><td style="background-color:transparent;padding-top:0;padding-bottom:0;padding-right:0;padding-left:0" class="mceBlockContainer" valign="top"><table border="0" cellpadding="0" cellspacing="0" width="100%" style="background-color:transparent" role="presentation" data-block-id="48"><tbody><tr><td style="min-width:100%;border-top:90px solid transparent" valign="top"></td></tr></tbody></table></td></tr><tr><td style="background-color:#6b9d51;padding-top:12px;padding-bottom:12px;padding-right:24px;padding-left:24px" class="mceBlockContainer" valign="top"><div data-block-id="40" class="mceText" id="dataBlockId-40" style="width:100%"><p style="text-align: left;" class="last-child"><strong><span style="color:#ffffff;"><span style="font-size: 21px">¿Qué es RPA y por qué es importante?</span></span></strong></p></div></td></tr><tr><td style="background-color:#6b9d51;padding-top:20px;padding-bottom:20px;padding-right:24px;padding-left:24px" class="mceBlockContainer" valign="top"><table border="0" cellpadding="0" cellspacing="0" width="100%" style="background-color:#6b9d51" role="presentation" data-block-id="41"><tbody><tr><td style="min-width:100%;border-top:2px solid #fbfbfb" valign="top"></td></tr></tbody></table></td></tr><tr><td style="background-color:#6b9d51;padding-top:12px;padding-bottom:12px;padding-right:24px;padding-left:24px" class="mceBlockContainer" valign="top"><div data-block-id="42" class="mceText" id="dataBlockId-42" style="width:100%"><p style="text-align: left;" class="last-child"><span style="color:#ffffff;"><span style="font-size: 19px">La Automatización de Procesos Robóticos es una tecnología revolucionaria que utiliza robots de software para automatizar tareas repetitivas y manuales en los procesos empresariales. Estos robots pueden realizar tareas complejas de manera eficiente y sin errores, liberando a los profesionales para que se centren en actividades más estratégicas y creativas.</span></span></p></div></td></tr></tbody></table></td><td style="padding-top:0;padding-bottom:0;margin-bottom:24px" class="mceColumn" data-block-id="38" valign="top" colspan="6" width="50%"><table border="0" cellpadding="0" cellspacing="0" width="100%" role="presentation"><tbody><tr><td style="padding-top:12px;padding-bottom:12px;padding-right:24px;padding-left:24px" class="mceBlockContainer" valign="top"><div data-block-id="43" class="mceText" id="dataBlockId-43" style="width:100%"><p style="text-align: left;" class="last-child"><strong><span style="color:#ffffff;"><span style="font-size: 17px">Nuestro Compromiso con la Innovación</span></span></strong></p></div></td></tr><tr><td style="padding-top:12px;padding-bottom:12px;padding-right:24px;padding-left:24px" class="mceBlockContainer" valign="top"><div data-block-id="44" class="mceText" id="dataBlockId-44" style="width:100%"><p style="text-align: left;" class="last-child"><span style="color:#ffffff;"><span style="font-size: 14px">En Pacandev, siempre hemos estado comprometidos con la innovación y la búsqueda de soluciones que mejoren la eficiencia y la productividad. La RPA es un paso natural en esa dirección. Estamos entusiasmados de comenzar a ofrecer servicios de RPA para ayudar a las empresas a optimizar sus operaciones y alcanzar nuevos niveles de eficiencia.</span></span></p></div></td></tr><tr><td style="background-color:transparent;padding-top:20px;padding-bottom:20px;padding-right:24px;padding-left:24px" class="mceBlockContainer" valign="top"><table border="0" cellpadding="0" cellspacing="0" width="100%" style="background-color:transparent" role="presentation" data-block-id="45"><tbody><tr><td style="min-width:100%;border-top:2px solid #ffffff" valign="top"></td></tr></tbody></table></td></tr><tr><td style="padding-top:12px;padding-bottom:12px;padding-right:24px;padding-left:24px" class="mceBlockContainer" valign="top"><div data-block-id="46" class="mceText" id="dataBlockId-46" style="width:100%"><p style="text-align: left;" class="last-child"><strong><span style="color:#ffffff;"><span style="font-size: 17px">Beneficios de la RPA con Pacandev</span></span></strong></p></div></td></tr><tr><td style="padding-top:12px;padding-bottom:12px;padding-right:24px;padding-left:24px" class="mceBlockContainer" valign="top"><div data-block-id="47" class="mceText" id="dataBlockId-47" style="width:100%"><ul class="last-child"><li style="color: #ffffff; text-align: left;"><p style="text-align: left;"><span style="color:#ffffff;"><span style="font-size: 15px">Automatización de tareas repetitivas.</span></span></p></li><li style="color: #ffffff; text-align: left;"><p style="text-align: left;"><span style="color:#ffffff;"><span style="font-size: 15px">Reducción de errores humanos.</span></span></p></li><li style="color: #ffffff; text-align: left;"><p style="text-align: left;"><span style="color:#ffffff;"><span style="font-size: 15px">Mayor eficiencia y productividad.</span></span></p></li><li style="color: #ffffff; text-align: left;"><p style="text-align: left;"><span style="color:#ffffff;"><span style="font-size: 15px">Ahorro de tiempo y recursos.</span></span></p></li><li style="color: #ffffff; text-align: left;"><p style="text-align: left;"><span style="color:#ffffff;"><span style="font-size: 15px">Enfoque en tareas estratégicas y creativas.</span></span></p></li><li style="color: #ffffff; text-align: left;"><p style="text-align: left;"><span style="color:#ffffff;"><span style="font-size: 15px">Integración con sistemas existentes.</span></span></p></li></ul></div></td></tr></tbody></table></td></tr></tbody></table></td></tr></tbody></table></td></tr></tbody></table></td></tr></tbody></table></td></tr></tbody></table></td></tr></tbody></table></td></tr></tbody></table></td></tr></tbody></table></td></tr><tr><td style="padding-top:12px;padding-bottom:12px;padding-right:24px;padding-left:24px" class="mceBlockContainer" valign="top"><div data-block-id="49" class="mceText" id="dataBlockId-49" style="width:100%"><p class="last-child"><strong>Estamos emocionados de embarcarnos en esta nueva era de innovación y eficiencia con la Automatización de Procesos Robóticos (RPA). Si estás interesado en conocer más sobre cómo la RPA puede transformar tu negocio y simplificar tus operaciones, ¡estamos aquí para ayudarte!</strong></p></div></td></tr><tr><td style="background-color:transparent;padding-top:20px;padding-bottom:20px;padding-right:24px;padding-left:24px" class="mceBlockContainer" valign="top"><table border="0" cellpadding="0" cellspacing="0" width="100%" style="background-color:transparent" role="presentation" data-block-id="50"><tbody><tr><td style="min-width:100%;border-top:2px solid #000000" valign="top"></td></tr></tbody></table></td></tr><tr><td style="padding-top:12px;padding-bottom:12px;padding-right:0;padding-left:0" class="mceLayoutContainer" valign="top"><table align="center" border="0" cellpadding="0" cellspacing="0" width="100%" role="presentation" data-block-id="51" id="section_5dc49fa388110f912da2bf2f3e31fe07" class="mceLayout"><tbody><tr class="mceRow"><td style="background-position:center;background-repeat:no-repeat;background-size:cover" valign="top"><table border="0" cellpadding="0" cellspacing="0" width="100%" role="presentation"><tbody><tr><td class="mceColumn" data-block-id="-18" valign="top" colspan="12" width="100%"><table border="0" cellpadding="0" cellspacing="0" width="100%" role="presentation"><tbody><tr><td align="center" valign="top"><table align="center" border="0" cellpadding="0" cellspacing="0" width="100%" role="presentation" data-block-id="-11"><tbody><tr class="mceRow"><td style="background-position:center;background-repeat:no-repeat;background-size:cover" valign="top"><table border="0" cellpadding="0" cellspacing="0" width="100%" role="presentation"><tbody><tr><td class="mceColumn" data-block-id="-24" valign="top" colspan="12" width="100%"><table border="0" cellpadding="0" cellspacing="0" width="100%" role="presentation"><tbody><tr><td valign="top"><table align="center" border="0" cellpadding="0" cellspacing="0" width="100%" role="presentation" data-block-id="56"><tbody><tr class="mceRow"><td style="background-position:center;background-repeat:no-repeat;background-size:cover;padding-top:0px;padding-bottom:0px" valign="top"><table border="0" cellpadding="0" cellspacing="24" width="100%" style="table-layout:fixed" role="presentation"><colgroup><col span="1" width="8.333333333333332%"><col span="1" width="8.333333333333332%"><col span="1" width="8.333333333333332%"><col span="1" width="8.333333333333332%"><col span="1" width="8.333333333333332%"><col span="1" width="8.333333333333332%"><col span="1" width="8.333333333333332%"><col span="1" width="8.333333333333332%"><col span="1" width="8.333333333333332%"><col span="1" width="8.333333333333332%"><col span="1" width="8.333333333333332%"><col span="1" width="8.333333333333332%"></colgroup><tbody><tr><td style="padding-top:0;padding-bottom:0" class="mceColumn" data-block-id="53" valign="top" colspan="6" width="50%"><table border="0" cellpadding="0" cellspacing="0" width="100%" role="presentation"><tbody><tr><td style="padding-top:12px;padding-bottom:12px;padding-right:24px;padding-left:24px" class="mceBlockContainer" valign="top"><div data-block-id="62" class="mceText" id="dataBlockId-62" style="width:100%"><p style="text-align: left;" class="last-child"><span style="font-size: 19px">¡Contacta a nuestro equipo de RPA hoy mismo y comencemos esta emocionante conversación!</span></p></div></td></tr></tbody></table></td><td style="padding-top:0;padding-bottom:0;margin-bottom:24px" class="mceColumn" data-block-id="55" valign="top" colspan="6" width="50%"><table border="0" cellpadding="0" cellspacing="0" width="100%" role="presentation"><tbody><tr><td style="padding-top:12px;padding-bottom:12px;padding-right:24px;padding-left:24px" class="mceBlockContainer" valign="top"><div data-block-id="58" class="mceText" id="dataBlockId-58" style="width:100%"><p style="text-align: left;" class="last-child"><strong><span style="font-size: 15px">Contáctanos</span></strong></p></div></td></tr><tr><td style="padding-top:12px;padding-bottom:12px;padding-right:24px;padding-left:24px" class="mceBlockContainer" align="right" valign="top"><table align="right" border="0" cellpadding="0" cellspacing="0" role="presentation" data-block-id="59"><tbody><tr class="mceStandardButton"><td style="background-color:#9bce76;border-radius:25px;text-align:center" class="mceButton" valign="top"><a href="tel:+57320 3455391" style="background-color:#9bce76;border-radius:25px;border:2px solid #6b9d51;color:#ffffff;display:block;font-family:&#39;Helvetica Neue&#39;, Helvetica, Arial, Verdana, sans-serif;font-size:16px;font-weight:bold;font-style:normal;padding:12px 28px;text-decoration:none;min-width:30px;text-align:center;direction:ltr;letter-spacing:0px">+57 3203455391</a></td></tr><tr>
<!--[if mso]>
<td align="right">
<v:roundrect xmlns:v="urn:schemas-microsoft-com:vml"
xmlns:w="urn:schemas-microsoft-com:office:word"
href="tel:+57320 3455391"
style="v-text-anchor:middle; width:179.78px; height:45.6px;"
arcsize="14%"
strokecolor="#6b9d51"
strokeweight="2px"
fillcolor="#9bce76">
<v:stroke dashstyle="solid"/>
<w:anchorlock />
<center style="
color: #ffffff;
display: block;
font-family: 'Helvetica Neue', Helvetica, Arial, Verdana, sans-serif;
font-size: 16;
font-style: normal;
font-weight: bold;
letter-spacing: 0px;
text-decoration: none;
text-align: center;
direction: ltr;"
>
+57 3203455391
</center>
</v:roundrect>
</td>
<![endif]-->
</tr></tbody></table></td></tr><tr><td style="padding-top:12px;padding-bottom:12px;padding-right:24px;padding-left:24px" class="mceBlockContainer" align="right" valign="top"><table align="right" border="0" cellpadding="0" cellspacing="0" role="presentation" data-block-id="60"><tbody><tr class="mceStandardButton"><td style="background-color:#9bce76;border-radius:25px;text-align:center" class="mceButton" valign="top"><a href="tel:+12023012527" style="background-color:#9bce76;border-radius:25px;border:2px solid #6b9d51;color:#ffffff;display:block;font-family:&#39;Helvetica Neue&#39;, Helvetica, Arial, Verdana, sans-serif;font-size:16px;font-weight:bold;font-style:normal;padding:12px 28px;text-decoration:none;min-width:30px;text-align:center;direction:ltr;letter-spacing:0px">+1 (202) 3012527</a></td></tr><tr>
<!--[if mso]>
<td align="right">
<v:roundrect xmlns:v="urn:schemas-microsoft-com:vml"
xmlns:w="urn:schemas-microsoft-com:office:word"
href="tel:+12023012527"
style="v-text-anchor:middle; width:185.98px; height:45.6px;"
arcsize="13%"
strokecolor="#6b9d51"
strokeweight="2px"
fillcolor="#9bce76">
<v:stroke dashstyle="solid"/>
<w:anchorlock />
<center style="
color: #ffffff;
display: block;
font-family: 'Helvetica Neue', Helvetica, Arial, Verdana, sans-serif;
font-size: 16;
font-style: normal;
font-weight: bold;
letter-spacing: 0px;
text-decoration: none;
text-align: center;
direction: ltr;"
>
+1 (202) 3012527
</center>
</v:roundrect>
</td>
<![endif]-->
</tr></tbody></table></td></tr></tbody></table></td></tr></tbody></table></td></tr></tbody></table></td></tr></tbody></table></td></tr></tbody></table></td></tr></tbody></table></td></tr></tbody></table></td></tr></tbody></table></td></tr></tbody></table></td></tr><tr><td style="background-color:transparent;padding-top:20px;padding-bottom:20px;padding-right:24px;padding-left:24px" class="mceBlockContainer" valign="top"><table border="0" cellpadding="0" cellspacing="0" width="100%" style="background-color:transparent" role="presentation" data-block-id="63"><tbody><tr><td style="min-width:100%;border-top:2px solid #000000" valign="top"></td></tr></tbody></table></td></tr><tr><td style="background-color:#6b9d51;padding-top:12px;padding-bottom:12px;padding-right:0;padding-left:0" class="mceLayoutContainer" valign="top"><table align="center" border="0" cellpadding="0" cellspacing="0" width="100%" role="presentation" data-block-id="65" id="section_9d40baaa53d5d3ae056d6635e5649cc9" class="mceLayout"><tbody><tr class="mceRow"><td style="background-position:center;background-repeat:no-repeat;background-size:cover" valign="top"><table border="0" cellpadding="0" cellspacing="0" width="100%" role="presentation"><tbody><tr><td class="mceColumn" data-block-id="-19" valign="top" colspan="12" width="100%"><table border="0" cellpadding="0" cellspacing="0" width="100%" role="presentation"><tbody><tr><td align="center" valign="top"><table align="center" border="0" cellpadding="0" cellspacing="0" width="100%" role="presentation" data-block-id="-13"><tbody><tr class="mceRow"><td style="background-position:center;background-repeat:no-repeat;background-size:cover" valign="top"><table border="0" cellpadding="0" cellspacing="0" width="100%" role="presentation"><tbody><tr><td class="mceColumn" data-block-id="-25" valign="top" colspan="12" width="100%"><table border="0" cellpadding="0" cellspacing="0" width="100%" role="presentation"><tbody><tr><td valign="top"><table align="center" border="0" cellpadding="0" cellspacing="0" width="100%" role="presentation" data-block-id="72"><tbody><tr class="mceRow"><td style="background-position:center;background-repeat:no-repeat;background-size:cover;padding-top:0px;padding-bottom:0px" valign="top"><table border="0" cellpadding="0" cellspacing="24" width="100%" style="table-layout:fixed" role="presentation"><colgroup><col span="1" width="8.333333333333332%"><col span="1" width="8.333333333333332%"><col span="1" width="8.333333333333332%"><col span="1" width="8.333333333333332%"><col span="1" width="8.333333333333332%"><col span="1" width="8.333333333333332%"><col span="1" width="8.333333333333332%"><col span="1" width="8.333333333333332%"><col span="1" width="8.333333333333332%"><col span="1" width="8.333333333333332%"><col span="1" width="8.333333333333332%"><col span="1" width="8.333333333333332%"></colgroup><tbody><tr><td style="padding-top:0;padding-bottom:0" class="mceColumn" data-block-id="67" valign="top" colspan="4" width="33.33333333333333%"><table border="0" cellpadding="0" cellspacing="0" width="100%" role="presentation"><tbody><tr><td style="padding-top:12px;padding-bottom:12px;padding-right:24px;padding-left:24px" class="mceBlockContainer" valign="top"><div data-block-id="73" class="mceText" id="dataBlockId-73" style="width:100%"><p class="last-child"><span style="color:#f8f3f3;">@pacandev</span></p></div></td></tr></tbody></table></td><td style="padding-top:0;padding-bottom:0" class="mceColumn" data-block-id="69" valign="top" colspan="4" width="33.33333333333333%"><table border="0" cellpadding="0" cellspacing="0" width="100%" role="presentation"><tbody><tr><td style="padding-top:12px;padding-bottom:12px;padding-right:24px;padding-left:24px" class="mceBlockContainer" valign="top"><div data-block-id="74" class="mceText" id="dataBlockId-74" style="width:100%"><p class="last-child"><a href="mailto:mjesus@pacandev.com" style="text-decoration: none;"><span style="color:#ffffff;">mjesus@pacandev.com</span></a></p></div></td></tr></tbody></table></td><td style="padding-top:0;padding-bottom:0;margin-bottom:24px" class="mceColumn" data-block-id="71" valign="top" colspan="4" width="33.33333333333333%"><table border="0" cellpadding="0" cellspacing="0" width="100%" role="presentation"><tbody><tr><td style="padding-top:12px;padding-bottom:12px;padding-right:24px;padding-left:24px" class="mceBlockContainer" valign="top"><div data-block-id="75" class="mceText" id="dataBlockId-75" style="width:100%"><p class="last-child"><a href="https://pacandev.com/" style="color: #ffffff; text-decoration: none;">pacandev.com</a></p></div></td></tr></tbody></table></td></tr></tbody></table></td></tr></tbody></table></td></tr></tbody></table></td></tr></tbody></table></td></tr></tbody></table></td></tr></tbody></table></td></tr></tbody></table></td></tr></tbody></table></td></tr><tr><td style="padding-top:8px;padding-bottom:8px;padding-right:8px;padding-left:8px" class="mceLayoutContainer" valign="top"><table align="center" border="0" cellpadding="0" cellspacing="0" width="100%" role="presentation" data-block-id="11" id="section_c6cbd89a5ea8bf8fa5b2b4af3f359760" class="mceFooterSection"><tbody><tr class="mceRow"><td style="background-position:center;background-repeat:no-repeat;background-size:cover" valign="top"><table border="0" cellpadding="0" cellspacing="12" width="100%" role="presentation"><tbody><tr><td style="padding-top:0;padding-bottom:0;margin-bottom:12px" class="mceColumn" data-block-id="-3" valign="top" colspan="12" width="100%"><table border="0" cellpadding="0" cellspacing="0" width="100%" role="presentation"><tbody><tr><td style="padding-top:12px;padding-bottom:12px;padding-right:48px;padding-left:48px" class="mceBlockContainer" align="center" valign="top"><img data-block-id="8" width="163.40640809443508" height="auto" style="width:163.40640809443508px;height:auto;max-width:100%;display:block" alt="Logo" src="cid:Mailtrapimage" class=""></td></tr><tr><td style="padding-top:12px;padding-bottom:12px;padding-right:16px;padding-left:16px" class="mceBlockContainer" align="center" valign="top"><div data-block-id="9" class="mceText" id="dataBlockId-9" style="display:inline-block;width:100%"><p class="last-child"><em><span style="font-size: 12px">Copyright (C) 2023 </span><span style="font-size: 13px">PacanDev</span><span style="font-size: 12px">. All rights reserved.</span></em><br><span style="font-size: 9px">En PacanDev, no solo creamos soluciones tecnológicas, creamos un futuro mejor. Permítenos ser tu socio en el viaje hacia la excelencia tecnológica y la transformación digital. Juntos, podemos hacer realidad tus sueños y alcanzar nuevos horizontes en el mundo digital.</span><br></tbody></table></td></tr></tbody></table></td></tr></tbody></table></td></tr></tbody></table></td></tr></tbody></table></td></tr></tbody></table></td></tr></tbody></table></td></tr></tbody></table></td></tr></tbody></table><!--[if (gte mso 9)|(IE)]></td></tr></table><![endif]--></td></tr></tbody></table>
</td>
</tr>
</tbody></table>
</center>

</body></html>
"""

f1 = open("f462772b-e426-e92b-5f2f-7f2cd45eecf9.png", 'rb')
image1 = MIMEImage(f1.read())
f1.close()
image1.add_header('Content-ID', '<Mailtrapimage>')
message.attach(image1)
#-----------------------------------------------
f2 = open("d3061b80-0b4a-9c30-c3af-ad03dbd0ab6e.png", 'rb')
image2 = MIMEImage(f2.read())
f2.close()
image2.add_header('Content-ID', '<Mailtrapimage2>')
message.attach(image2)






# Agregar el contenido HTML al mensaje
html_part = MIMEText(html, "html")
message.attach(html_part)






# Crear una conexión segura con el servidor SMTP
context = ssl.create_default_context()

# Enviar el mensaje a los destinatarios de la lista
import time
for i in lista:
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(
            sender_email, i, message.as_string()
        )
    time.sleep(20)
