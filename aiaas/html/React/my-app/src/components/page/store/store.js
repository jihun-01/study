// ../../components/page/store/store.js
import React, { useEffect } from 'react';
import styles from './store.module.css';
import Card400 from '../../common/itemcard/card400';
import Card480 from '../../common/itemcard/card480';
import Card313 from '../../common/itemcard/card313';
import Button from '../../common/button/button';
import ScrollButton from '../../common/button/scrollbutton'
import { useHeader } from '../../../contexts/HeaderContext';

const StoreHome = () => {
 
    return (
        <>
            <main className={styles.storehome}>
                {/*헤더*/}
                <div className={styles.storehome_header}>
                    <div className={styles.storehome_header_left}>
                        <div className={styles.storehome_header_left_title}>
                            <span className={styles.storehome_title_main_text_black}>스토어.</span>
                            <span className={styles.storehome_title_main_text_gray}>좋아하는 Apple 제품을 구입하는 가장 좋은 방법.</span>
                        </div>
                    </div>
                    <div className={styles.storehome_header_right}>
                        <section className={styles.storehome_header_right_chat}>
                            <div className={styles.storehome_header_right_chat_img}>
                                <img width="35" height="35" alt="" src="https://store.storeimages.cdn-apple.com/1/as-images.apple.com/is/store-chat-earth-day-specialist-icon-202504_AV4?wid=70&amp;hei=70&amp;fmt=jpeg&amp;qlt=90&amp;.v=MGlSYzZEcVYyWHpqdksxSCs4YjFLNzBQSmhWRTJPSGNQRHRFQ0RoYnJFNEtUTWVRaGpWVmhKOG83bW9wSUVGNXdpTHZxMWM3WWRmQnVUWUQ0V2tXSjdrNkxqcEdrM2x6OUZ3Z2JnTllhUU5XS0ZMbkg4ZVBxKzVXaGU3eFBVQnI"/>
                            </div>
                            <div className={styles.storehome_header_right_chat_text_container}>
                                <div className={styles.storehome_header_right_chat_text}>
                                    <p>쇼핑 지원이 필요하다면?</p>
                                </div>
                                <div className={styles.storehome_header_right_chat_link}>
                                <a href="#">스페셜리스트에게 문의하세요</a>
                                </div>
                            </div>
                        </section>
                        <section className={styles.storehome_header_right_chat}>
                            <div className={styles.storehome_header_right_chat_img}>
                                <svg width="25" height="35" viewBox="0 0 25 35" aria-hidden="true">
                                    <path d="m0 0h25v35h-25z" fill="none"></path>
                                    <path d="m12.4934 4.675a10.5617 10.5617 0 0 1 4.177.8275 10.8868 10.8868 0 0 1 5.7467 5.747 10.4988 10.4988 0 0 1 .8329 4.1777 10.3219 10.3219 0 0 1 -.6421 3.5951 10.8948 10.8948 0 0 1 -1.8669 3.2062 12.8406 12.8406 0 0 1 -2.9537 2.5775c-.984.6179-1.8226 1.1843-2.4931 1.6839a9.5187 9.5187 0 0 0 -1.7742 1.6788 6.8587 6.8587 0 0 0 -1.02 1.8034 6.8213 6.8213 0 0 0 -1.0278-1.8062 9.8247 9.8247 0 0 0 -1.7708-1.6742c-.6644-.4987-1.5014-1.0658-2.485-1.6834a12.5961 12.5961 0 0 1 -2.9617-2.5777 10.99 10.99 0 0 1 -1.8636-3.2083 10.3421 10.3421 0 0 1 -.6411-3.5951 10.5153 10.5153 0 0 1 .8319-4.1772 10.9669 10.9669 0 0 1 2.3209-3.4333 10.85 10.85 0 0 1 3.4278-2.3142 10.52 10.52 0 0 1 4.1628-.8275m0-1a11.4634 11.4634 0 0 0 -4.5561.9081 11.89 11.89 0 0 0 -6.2738 6.2709 11.4566 11.4566 0 0 0 -.9135 4.5732 11.2871 11.2871 0 0 0 .703 3.9416 11.9349 11.9349 0 0 0 2.0323 3.5006 13.5349 13.5349 0 0 0 3.1956 2.7835q1.446.9079 2.42 1.6384a8.7962 8.7962 0 0 1 1.5912 1.5 5.9225 5.9225 0 0 1 .9731 1.81q.25.7236.8285.7238t.8417-.7238a5.9779 5.9779 0 0 1 .967-1.81 8.4991 8.4991 0 0 1 1.59-1.5q.98-.73 2.4268-1.6384a13.7877 13.7877 0 0 0 3.19-2.7835 11.8367 11.8367 0 0 0 2.0373-3.5006 11.263 11.263 0 0 0 .7041-3.9416 11.44 11.44 0 0 0 -.9145-4.5732 11.8867 11.8867 0 0 0 -6.2717-6.2709 11.5044 11.5044 0 0 0 -4.57-.9081zm3.8566 9.71a2.3254 2.3254 0 0 0 -1.078 1.94 2.2152 2.2152 0 0 0 1.353 2.0506 4.7326 4.7326 0 0 1 -.693 1.4443c-.429.6174-.902 1.2458-1.584 1.2458-.693 0-.858-.4079-1.661-.4079-.77 0-1.045.4189-1.672.4189-.638 0-1.078-.5733-1.584-1.29a6.3114 6.3114 0 0 1 -1.056-3.3625 2.7185 2.7185 0 0 1 2.541-3.0208c.682 0 1.232.441 1.65.441.407 0 1.023-.4631 1.782-.4631a2.3483 2.3483 0 0 1 2.002 1.0036zm-3.729-1.1135c-.055 0-.099-.0111-.143-.0111 0-.033-.011-.11-.011-.1874a2.26 2.26 0 0 1 .561-1.3781 2.19 2.19 0 0 1 1.485-.7717 1.0735 1.0735 0 0 1 .011.1984 2.3284 2.3284 0 0 1 -.528 1.4222 1.9664 1.9664 0 0 1 -1.375.7276z"></path>
                            </svg>
                            </div>
                            <div className={styles.storehome_header_right_chat_text_container}>
                                <div className={styles.storehome_header_right_chat_text}>
                                    <p>Apple Store를 방문하세요</p>
                                </div>
                                <div className={styles.storehome_header_right_chat_link}>
                                    <a href="#">가까운 매장 찾기</a>
                                </div>
                            </div>
                        </section>
                    </div>
                </div>
                {/*스크롤 아이템*/}
                <div className={styles.storehome_scroll_item}>
                    <div className={styles.storehome_scroll_item_container}>
                        <div className={styles.storehome_scroll_item_container_card_front}></div>
                        <div className={styles.storehome_scroll_item_container_card}>
                            <a href="#">
                                <div className={styles.storehome_scroll_item_container_img}>
                                    <img src="https://store.storeimages.cdn-apple.com/1/as-images.apple.com/is/store-card-13-mac-nav-202503?wid=400&hei=260&fmt=png-alpha&.v=M1Q3OGxnb1lBaHhqNjZ2OVRXZmx4VEpBUDFBeEhMZS9GUnNSYXdEd0hscisrUlZaSVRoWVYzU0Qra0FoTmUwNng2bitObzZwQzk4cEorV1dZdzhIazVVcFlOTkdoMWg4ZkdDS1ovMUlzcW8"/>
                                </div>
                                <div className={styles.storehome_scroll_item_container_img_text}>
                                    Mac
                                </div>
                            </a>
                        </div>
                        <div className={styles.storehome_scroll_item_container_card}>
                            <a href ="#">
                                <div className={styles.storehome_scroll_item_container_img}>
                                    <img src="https://store.storeimages.cdn-apple.com/1/as-images.apple.com/is/store-card-13-iphone-nav-202502?wid=400&hei=260&fmt=png-alpha&.v=dW5XbHI1eDVpd01qWUU4bFRtWGZXOG9vbGw5MnhRZ3BpYVMwQTIvb2xsaDVoZlhhY1p4QWdsTjFNaGRHM3FYWW15d1FhSDJ0bkR0ZGZtUjZJNmFveFVockp1czQ4Q0pvWUU1bC9ERnl2dFE"/>
                                </div>
                                <div className={styles.storehome_scroll_item_container_img_text}>
                                        <p>iPhone</p>
                                </div>
                            </a>        
                        </div>
                        <div className={styles.storehome_scroll_item_container_card}>
                            <a href="#">
                                <div className={styles.storehome_scroll_item_container_img}>
                                    <img src="https://store.storeimages.cdn-apple.com/1/as-images.apple.com/is/store-card-13-ipad-nav-202405?wid=400&hei=260&fmt=png-alpha&.v=dW5XbHI1eDVpd01qWUU4bFRtWGZXNGFLQTJVNnlNQmQrVmRBYnZYei9jckUzelNmMnRxajE0NHhmMWtLazl6eG53M0FRZHBXNTh1U1lFVEtSR2YzTm5qbE56RWRpRFNIRXZvbkd2S0l5dTg"/>
                                </div>
                                <div className={styles.storehome_scroll_item_container_img_text}>
                                    <p>iPad</p>
                                </div>
                            </a>
                        </div>
                        <div className={styles.storehome_scroll_item_container_card}>
                            <a href="#">
                                <div className={styles.storehome_scroll_item_container_img}>
                                    <img src="https://store.storeimages.cdn-apple.com/1/as-images.apple.com/is/store-card-13-watch-nav-202409?wid=400&hei=260&fmt=png-alpha&.v=S0tSVzBtSkRkSFFhMm1zS1NmeWtkNDJNVmlnVytwalkvOTJ2M1BKWUREdkh5NTJ6cGtEemJOblBHR043ZjFkZzAzOVFHb3N0MkVmS01ZcFh0d1Y4R2oxdUo4aWtyK05IRkZuWjBWbW5HM00"/>
                            </div>
                            <div className={styles.storehome_scroll_item_container_img_text}>
                                    <p>Apple Watch</p>
                            </div>
                            </a>
                        </div>
                        <div className={styles.storehome_scroll_item_container_card}>
                            <a href="#">
                                <div className={styles.storehome_scroll_item_container_img}>
                                    <img src="https://store.storeimages.cdn-apple.com/1/as-images.apple.com/is/store-card-13-vision-pro-nav-202401?wid=400&hei=260&fmt=png-alpha&.v=VzVpanYvTldHb05iVXFhc0xveWRLM25jd0w4dXFwc1hFbWZkNm9IcUR2bytSMWt1ZUNyTGx4SjRKL1pSL0ZDeGpCeVFkSWhuN0RJazJDeHBqaFFac0hlZzcwajlwb1R2dHNlazl1dldSUGQ5RzBLTDk5c25YRG5wR2ZpUlI4RFM"/>
                                </div>
                                <div className={styles.storehome_scroll_item_container_img_text}>
                                    <p>Vision Pro</p>
                                </div>
                            </a>
                        </div>
                        <div className={styles.storehome_scroll_item_container_card}>
                            <a href="#">
                                <div className={styles.storehome_scroll_item_container_img}>
                                    <img src="https://store.storeimages.cdn-apple.com/1/as-images.apple.com/is/store-card-13-airpods-nav-202409?wid=400&hei=260&fmt=png-alpha&.v=Q0Z1bWFqMUpRRnp3T0Y0VWJpdk1yNlJ5eGFhR1FVd2NNNDB0VWRUSzVCUFd1aTN5QlRYNG5PRjJxc2d1RklXbVM0TjRWdzF2UjRGVEY0c3dBQVZ6VFI0R1M4eFpKRTFIclV0ZHRqakVRd1k"/>
                                </div>
                                <div className={styles.storehome_scroll_item_container_img_text}>
                                     <p>AirPods</p>
                                </div>
                            </a>
                        </div>
                        <div className={styles.storehome_scroll_item_container_card}>
                            <a href="#">
                                <div className={styles.storehome_scroll_item_container_img}>
                                    <img src="https://store.storeimages.cdn-apple.com/1/as-images.apple.com/is/store-card-13-airtags-nav-202108?wid=400&hei=260&fmt=png-alpha&.v=Q0Z1bWFqMUpRRnp3T0Y0VWJpdk1ydzduWDk4YUM5R1JVL2gwcEZnWWNaRFd1aTN5QlRYNG5PRjJxc2d1RklXbVM0TjRWdzF2UjRGVEY0c3dBQVZ6VFpQclc0OVE3cmhmS3FBaXd6cG8yYzg"/>
                                </div>
                                <div className={styles.storehome_scroll_item_container_img_text}>
                                        <p>AirTags</p>
                                </div>
                            </a>
                        </div>
                        <div className={styles.storehome_scroll_item_container_card}>
                            <a href="#">
                                <div className={styles.storehome_scroll_item_container_img}>
                                <img src="https://store.storeimages.cdn-apple.com/1/as-images.apple.com/is/store-card-13-appletv-nav-202210?wid=400&hei=260&fmt=png-alpha&.v=T0wvM1N3YUcxQ09qK0VNRkl1RU1BZFM5WnN0RmVZRmVXQ0FCUWJjbnJDald1aTN5QlRYNG5PRjJxc2d1RklXbVM0TjRWdzF2UjRGVEY0c3dBQVZ6VFZ3YmJrVi9SakQxWUcrYWQwVXc5VTA"/>
                                </div>
                                <div className={styles.storehome_scroll_item_container_img_text}>
                                    <p>Apple TV 4K</p>
                                </div>
                            </a>
                        </div>
                        <div className={styles.storehome_scroll_item_container_card}>
                            <a href="#">
                                <div className={styles.storehome_scroll_item_container_img}>
                                <img src="https://store.storeimages.cdn-apple.com/1/as-images.apple.com/is/store-card-13-accessories-nav-202503?wid=400&hei=260&fmt=png-alpha&.v=QnhsNk96S0o4R1dkN2FveStNM1hwNzZGMHVrNGw2NTM5Vmk2bHZzMXQ3aUJGVHdnWkxMaklDeW9JYU5tT3FWeVBrcjVFNVdueFRVbVY3TGtiL2RjUVhQYS92MS9scmN4eTZLbFFkMHVzTVhuL2FLN3hwSUJhbzdFUHltVU1ldnQ"/>
                            </div>
                                <div className={styles.storehome_scroll_item_container_img_text}>
                                    <p>액세서리</p>
                                </div>
                            </a>
                        </div>
                    </div>
                </div>
                {/*최신 제품 소개*/}
                <div className={styles.storehome_latest_product}>
                    <div className={styles.storehome_latest_product_title}>
                        <span className={styles.storehome_title_text_black}>최신 제품.</span>
                        <span className={styles.storehome_title_text_gray}>따끈따끈한 신제품 이야기.</span>
                    </div>
                    <ScrollButton className={styles.storehome_scroll_product}>
                    <div className={styles.storehome_latest_product_card_container}>
                        <div className={styles.list_item}>
                            <div className={styles.storehome_latest_product_card}>
                            <Card400 name="MacBook Air" describe="Apple Intelligence" price="₩1,590,000부터" path="#" image="https://store.storeimages.cdn-apple.com/1/as-images.apple.com/is/store-card-40-macbook-air-202503?wid=800&hei=1000&fmt=p-jpg&qlt=95&.v=MjhMcWJ2MGZwbXEwdnBkcUN6ZnhyOWVOMytmanI1M0ZTQWR1RjlDMWJpNXFTRjNxbmh1UnU2R29ibGdpZUFXc0prY3crUWRsN1dqVjRnMHR5S1hVbk15N0N0R0lhUGhlMG1Tdmc3RjZVQ09NTUhYNlZ6OGxKNWpBMHlTSTlldko"/>
                            </div>
                        </div>
                        <div className={styles.list_item}>
                            <div className={styles.storehome_latest_product_card}>
                            <Card400 name="iPhone 16 Pro" nameType="white" describe="Apple Intelligence" price="₩1,550,000부터" priceType="white" path="#" image="https://store.storeimages.cdn-apple.com/1/as-images.apple.com/is/store-card-40-iphone-16-pro-202409?wid=800&hei=1000&fmt=jpeg&qlt=90&.v=UzBXQnlhUWdraTNvNU1Kb3pEQlpXUHpnd0VsRWFiaWRaRHRaUXBvNTNkalNab1lJcUZwSFVRK1htYlNmZUtPTG54cStVNU5BQmhzbkxYRGxDWUc3R1lXVzNzT2dSajRTd2tFaEdoYUp2VnY1WVJVT21DTzBZRFlBTTZySFFMbHY"/>
                            </div>
                        </div>
                        <div className={styles.list_item}>
                            <div className={styles.storehome_latest_product_card}>
                            <Card400 name="iPad Air" describeType="black" describe="바람처럼 빠르게" price="₩949,000부터" path="#" image="https://store.storeimages.cdn-apple.com/1/as-images.apple.com/is/store-card-40-ipad-air-202503?wid=800&hei=1000&fmt=p-jpg&qlt=95&.v=UzBXQnlhUWdraTNvNU1Kb3pEQlpXRFJ0OFRiWngrNGllYTMvQ1dlWDBQZjZXYXJlRUd1cTBYTnRnbTNlazIvMzRHeXB5TnVsU3R6Qjd0Y2JzbURyWEdJV2RaUklyUnViT0c4OGJXRWhUTnArYWpGdS9XeFgvbS9ITnNYOEhYaG4"/>
                            </div>
                        </div>
                        <div className={styles.list_item}>
                            <div className={styles.storehome_latest_product_card}>
                            <Card400 name="Apple Watch 프라이드 에디션 스포츠 밴드" describeType="black" describe="무지갯빛으로 당당하게." price="₩65,000" path="#" image="https://store.storeimages.cdn-apple.com/1/as-images.apple.com/is/store-card-40-watch-pride-202505?wid=800&hei=1000&fmt=png-alpha&.v=QWhYaUFuRS9hTUliZ3N5RWVCV09vdDYvU0ZacGROckNJUjJGMTk0bnRxaHFTRjNxbmh1UnU2R29ibGdpZUFXc3V5NVU0QmM2b3hmeWJWTTVtN1o5ZnNZK25GTnpvbUY1UTI4WmI2VjkwM1YrYWpGdS9XeFgvbS9ITnNYOEhYaG4"/>
                            </div>
                        </div>
                        <div className={styles.list_item}>
                            <div className={styles.storehome_latest_product_card}>
                            <Card400 name="Apple Watch Series 10" describeType="black" describe="얇아진 두께. 더 커진 존재감." price="₩599,000부터" path="#" image="https://store.storeimages.cdn-apple.com/1/as-images.apple.com/is/store-card-40-watch-s10-202409?wid=800&hei=1000&fmt=jpeg&qlt=90&.v=QWhYaUFuRS9hTUliZ3N5RWVCV09vbGtrQjBqdmhJbWlLcCtlQTMwc01SdjkvamYzRzRvcFlnajNacmhEOC9BeDE1UUxLT2t0cW42N3FvQzVqaGhrVVlSek45NHpYUG91NnZ3YmlDQlpUYnArYWpGdS9XeFgvbS9ITnNYOEhYaG4"/>
                            </div>
                        </div>
                        <div className={styles.list_item}>
                            <div className={styles.storehome_latest_product_card}>
                            <Card400 name="iPhone 16e" describe="Apple Intelligence" price="₩990,000부터" path="#" image="https://store.storeimages.cdn-apple.com/1/as-images.apple.com/is/store-card-40-iphone-16e-202502_GEO_KR?wid=800&hei=1000&fmt=jpeg&qlt=90&.v=UzBXQnlhUWdraTNvNU1Kb3pEQlpXSzRWdVVUSklyLzFIUnk0cUZLSXhCVnRDKzU3amEwWnp2K0RPZm52QW9wL1JSeXJaL3JqNm9jc2psYU5Qelh0TnNldk5NTXRkeFF2V3BGOGlmVi9OaUE1YlplWFJuaTJ3ajR1TFNMNDJGK2U"/>                           
                            </div>
                        </div>
                        <div className={styles.list_item}>
                            <div className={styles.storehome_latest_product_card}>
                            <Card400 name="iPad" describeType="black" describe="쓰다. 그리다. 빠져들다." price="₩529,000부터" path="#" image="https://store.storeimages.cdn-apple.com/1/as-images.apple.com/is/store-card-40-ipad-202503_GEO_KR?wid=800&hei=1000&fmt=jpeg&qlt=90&.v=UzBXQnlhUWdraTNvNU1Kb3pEQlpXRC9uRDZRd1JCWThWeW95ZThtaUk5OXFTRjNxbmh1UnU2R29ibGdpZUFXcy85S3R4M0M3WGhIQVNOK3lBdUI5K2ZQbDhZb2VjNVFtNU9iWEJjMWZNcW1jMkZpM21VaDE5elJ5N3JKNUFtcWI"/>                           
                            </div>
                        </div>
                        <div className={styles.list_item}>
                            <div className={styles.storehome_latest_product_card}>
                            <Card400 name="Mac Studio" describe="Apple Intelligence" price="₩3,290,000부터" path="#" image="https://store.storeimages.cdn-apple.com/1/as-images.apple.com/is/store-card-40-mac-studio-202503?wid=800&hei=1000&fmt=p-jpg&qlt=95&.v=MjhMcWJ2MGZwbXEwdnBkcUN6ZnhyMFozSSthUWxLelAxTitDZ3M4Tk5nbm45S05qekNUdVUwMVFyK1pKaERUd3NtS0NkZnlUKzBRdlpRai9zMDR0cTA2K1VNZGNlb0hPLzMyemJjWVkyQ0JMQzBoZ1NYMmRGQ2VZWXI2YVMzc2I"/>                           
                            </div>
                        </div>
                        <div className={styles.list_item}>
                            <div className={styles.storehome_latest_product_card}>
                            <Card400 name="iPhone 16" nameType="white" describe="Apple Intelligence" price="₩1,250,000부터" priceType="white" path="#" image="https://store.storeimages.cdn-apple.com/1/as-images.apple.com/is/store-card-40-iphone-16-202409?wid=800&hei=1000&fmt=jpeg&qlt=90&.v=UzBXQnlhUWdraTNvNU1Kb3pEQlpXSHNhd1RFMExoRHFBcWNCalJOblBtbjkvamYzRzRvcFlnajNacmhEOC9BeDE1UUxLT2t0cW42N3FvQzVqaGhrVVQ1UEcwSy9Yd3FpT0wveFRydDk3cE4rYWpGdS9XeFgvbS9ITnNYOEhYaG4"/>                           
                            </div>
                        </div>
                        <div className={styles.list_item}>
                            <div className={styles.storehome_latest_product_card}>
                            <Card400 name="Apple Watch Ultra 2" nameType="white" describeType="white" describe="블랙으로 계속되는 전력 질주." price="₩1,149,000부터" priceType="white" path="#" image="https://store.storeimages.cdn-apple.com/1/as-images.apple.com/is/store-card-40-watch-ultra-202409_GEO_KR?wid=800&hei=1000&fmt=jpeg&qlt=90&.v=QWhYaUFuRS9hTUliZ3N5RWVCV09vbHdYN09OOVhGMkJZZWFPTlJDYlZ0VkFYdUFnVlgvUCtkRUM4dVJJUkRxSHAwckMxbExydC8yeDhtUjlFVHdKVnRSR0liZklwWjJ2eGlOd1dxRHFuOXFZUFpIL004NVhDbUZOOW82a2p5cS8"/>                           
                            </div>
                        </div>
                        <div className={styles.list_item}>
                            <div className={styles.storehome_latest_product_card}>
                            <Card400 text="Apple Watch 밴드" name="다양한 스타일. 다양한 컬러."  path="#" image="https://store.storeimages.cdn-apple.com/1/as-images.apple.com/is/store-card-40-watch-bands-202503?wid=800&hei=1000&fmt=p-jpg&qlt=95&.v=QWhYaUFuRS9hTUliZ3N5RWVCV09va1BWaWtDc3JqbmtIWDhTOVFud0xCSnFTRjNxbmh1UnU2R29ibGdpZUFXc0prY3crUWRsN1dqVjRnMHR5S1hVbkRMUVYvUzMyczZzTlBKNTVVYUNsRytycDU0Zm9tS1NLYWZhaWJKS1VJSUo"/>                           
                            </div>
                        </div>
                    </div>
                    </ScrollButton>
                </div>
                {/*도움 카드*/}
                <div className={styles.storehome_help_card}>
                    <div className={styles.storehome_help_card_title}>
                        <span className={styles.storehome_title_text_black}>도움의 손길.</span>
                        <span className={styles.storehome_title_text_gray}>언제든, 당신에게 맞는 방식으로.</span>
                    </div>
                    <div className={styles.storehome_help_card_container}>
                        <div className={styles.storehome_help_card_container_card}>
                            <Card480 text="Apple 스페셜리스트" name="스페셜리스트와 함께하는 일대일 온라인 쇼핑." path="#" image="https://store.storeimages.cdn-apple.com/1/as-images.apple.com/is/store-card-50-earth-day-specialist-help-202504?wid=4000&hei=4167&fmt=p-jpg&qlt=95&.v=cHZTdEJURVNIcmNmcWQ1YlUyV2pSZmZ6Q2ZTaDM0dDFtQTRQZitiSUxoQ3ZaQ3BPZ3VPbjZ1OE1jMHB0VHplaVQ1SVRRZnoyY2xiVHFIbFpnUnJwcmJKaWduWDhrL3RFTDJVSS83Tk9MYXNncFNxekt2MjNBWmdPdTJsTW1wWDdOcEJRdUlLK3pHczBBRDF3cDFHQ3Bn"/>
                        </div>
                        <div className={styles.storehome_help_card_container_card}>
                            <Card480 text="TODAY AT APPLE" name="꼭 맞는 손쉬운 사용 세션 예약하기." describe="무료 세션을 예약하고, 누구나 자기만의 방식대로 Apple 기기를 활용할 수 있도록 도와주는 내장 기능들을 알아보세요." path="#" image="https://store.storeimages.cdn-apple.com/1/as-images.apple.com/is/store-card-50-taa-gaad-202505?wid=960&hei=1000&fmt=p-jpg&qlt=95&.v=cFEvalhFakpZVzg4RFZsWktqbXFNY0c2by9KWHE0U1NmaEtuWndhZksrQ2o2Z1ptREdBenZRTjZuSCtBemFnUTRHeXB5TnVsU3R6Qjd0Y2JzbURyWFA2Q2ZXNGtMc2tNc1puZEN0QmlFbFIrYWpGdS9XeFgvbS9ITnNYOEhYaG4"/>
                        </div>
                        <div className={styles.storehome_help_card_container_card}>
                            <Card480 text="개인 맞춤 설정" name="새 기기 설정은 스페셜리스트의 도움과 함께." describe="데이터 전송 방법부터 최신 기능 사용법까지 온라인 일대일 세션에서 자세히 안내해 드립니다" path="#" image="https://store.storeimages.cdn-apple.com/1/as-images.apple.com/is/store-card-50-personal-setup-202408_GEO_KR?wid=960&hei=1000&fmt=p-jpg&qlt=95&.v=cFhHZjJBWFBWT2pMQnNFR2RGWlEwWlNLRUlsMkFxY1ZMQzZzY0tkenJrbVpUcktud3gyRlFwYlRKZ0M1UzloMlM3UUxhTDY4VmxnT1pqOEpldm1McjB0RmgycTRGTHI3SUVxVFVFNFI5QzlDblhqYnJabTUrNUtXVTZ0M1lPRzM"/>
                        </div>
                        <div className={styles.storehome_help_card_container_card}>
                            <Card480 name="Genius Bar에서 직접 전문가의 도움을 받을 수 있습니다." path="#" image="https://store.storeimages.cdn-apple.com/1/as-images.apple.com/is/store-card-50-genius-202108?wid=960&hei=1000&fmt=p-jpg&qlt=95&.v=UjZWNjB3VDZRK09HelFpSjJDWXROSXFFVHJmY3pQTE80cGIxc1pFQ1VBQWYzUHRVc053YldlK2NuZForb0M1V0tRNjVHZTlIV04vVjZjbEh0Rm5SYzRmTnpyOVBFZDFPdWR2WFZpUzNkaDA"/>
                        </div>
                    </div>
                </div>
                {/*쇼핑 카드*/}
                <div className={styles.storehome_shopping_reason}>
                    <div className={styles.storehome_shopping_reason_header}>
                        <span className={styles.storehome_title_text_black}>남다른 Apple Store.</span>
                        <span className={styles.storehome_title_text_gray}>이곳에서 쇼핑해야 하는 더욱더 많은 이유.</span>
                    </div>
                    <div className={styles.storehome_shopping_reason_main}>
                        <div className={styles.storehome_shopping_reason_card}>
                            <div className={styles.storehome_shopping_reason_card_container}>
                                <div className={styles.storehome_shopping_reason_card_container_card}>
                                    <div className={styles.storehome_shopping_reason_card_container_icon}>
                                        <svg width="46" height="56" viewBox="0 0 46 56" className={styles.card_icon} aria-hidden="true">
                                            <path d="M41.0009,12H5A5,5,0,0,0,.0009,17L0,39a5,5,0,0,0,4.9991,5H41.0009A5,5,0,0,0,46,39V17A5,5,0,0,0,41.0009,12ZM5,14H41.0009A3.0032,3.0032,0,0,1,44,17l.0005,2H2l.0005-2A3.0032,3.0032,0,0,1,5,14ZM41.0009,42H4.9991a3.0032,3.0032,0,0,1-3-3V22.9577H44V39A3.0032,3.0032,0,0,1,41.0009,42ZM15,31.5737v3.8526A1.5541,1.5541,0,0,1,13.4663,37H8.5338A1.5542,1.5542,0,0,1,7,35.4263V31.5737A1.5542,1.5542,0,0,1,8.5338,30h4.9325A1.5541,1.5541,0,0,1,15,31.5737Z"></path>
                                        </svg>
                                    </div>
                                    <div className={styles.storehome_shopping_reason_card_container_text}>
                                        기분 좋은 결제 옵션.
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div className={styles.storehome_shopping_reason_card}>
                            <div className={styles.storehome_shopping_reason_card_container}>
                                <div className={styles.storehome_shopping_reason_card_container_card}>
                                    <div className={styles.storehome_shopping_reason_card_container_icon}>
                                        <svg width="40" height="56" viewBox="0 0 40 56" className={styles.card_icon_elevated} aria-hidden="true">
                                            <path d="m0 0h40v56h-40z" fill="none"></path>
                                            <path d="m38 29.0205v9.9795c0 3.8594-3.1403 7-6.9996 7h-22c-3.8594 0-7-3.1406-7-7v-4.75h-1.2514c-.7087 0-.8958-.4824-.502-1.0337l2.2051-3.1304c.315-.4529.7875-.443 1.1025 0l2.2051 3.1403c.3839.5414.1969 1.0238-.5021 1.0238h-1.2576v4.75c0 2.7568 2.2435 5 5.0004 5h22c2.7568 0 5-2.2432 5-5v-9.9795c0-.5527.4473-1 1-1s.9996.4473.9996 1zm1.251-7.2705h-1.251v-4.75c0-3.8594-3.1403-7-6.9996-7h-22c-3.8594 0-7 3.1406-7 7v9.9795c0 .5527.4473 1 1 1s.9996-.4473.9996-1v-9.9795c0-2.7568 2.2435-5 5.0004-5h22c2.7568 0 5 2.2432 5 5v4.75h-1.258c-.6989 0-.886.4823-.502 1.0237l2.2051 3.1404c.315.4429.7875.4529 1.1025 0l2.2051-3.1305c.3937-.5513.2067-1.0336-.5021-1.0336zm-13.8013 1.6872c.2991-.2918.7214-.4372 1.2668-.4372h3.569c.5396 0 .9599.1454 1.261.4372.303.2918.4536.7004.4536 1.225v8.6845c0 .5246-.1486.9313-.4477 1.2201s-.7214.4332-1.2668.4332h-3.569c-.5454 0-.9677-.1444-1.2668-.4332s-.4496-.6955-.4496-1.2201v-8.6845c0-.5246.1505-.9333.4496-1.225zm.7038 9.7945c0 .2004.0469.3517.1447.4548.0958.1032.2424.1552.436.1552h3.524c.1935 0 .3402-.0521.4398-.1552.0997-.1032.1506-.2544.1506-.4548v-8.4546c0-.2004-.0508-.3537-.1506-.4598-.0997-.1061-.2463-.1591-.4398-.1591h-3.524c-.1935 0-.3402.053-.436.1591-.0977.1061-.1447.2593-.1447.4598zm2.3488-13.2317h-16.6196c-.5806 0-1.0401.1572-1.3773.4725s-.5054.783-.5054 1.4019v11.1256h-1.2559c-.2757 0-.5103.0824-.7038.2798s-.2903.4352-.2903.7122.0968.5138.2903.7122c.1935.1965.4281.2957.7038.2957h15.1703c-.2581-.4126-.393-.8841-.4047-1.4146 0-.1002-.002-.2004-.0059-.3006-.002-.1002-.0039-.1846-.0039-.2848h-12v-10.6512c0-.2829.0704-.4951.2111-.6366s.3519-.2122.6334-.2122h17.7686c-.0352-.4715-.1916-.9037-.4672-1.1424s-.6569-.3576-1.1437-.3576zm-.6924 5.4067h1.3802c.1114 0 .2072-.0403.2854-.1199.0801-.0796.1193-.1778.1193-.2957 0-.112-.0391-.2063-.1193-.2829-.0782-.0766-.174-.1149-.2854-.1149h-1.3802c-.1173 0-.215.0383-.2913.1149s-.1134.1709-.1134.2829c0 .1179.0371.2161.1134.2957s.174.1199.2913.1199zm-.4179 7.8983h2.2c.1887 0 .284-.1032.284-.3095 0-.0884-.027-.1611-.0809-.2171s-.1222-.0835-.2031-.0835h-2.2c-.0809 0-.1456.0275-.1941.0835s-.0719.1287-.0719.2171c0 .2063.0881.3095.266.3095z"></path>
                                        </svg>
                                    </div>
                                    <div className={styles.storehome_shopping_reason_card_container_text}>
                                        쓰던 기기를 보상 판매하고 새 기기를 더 저렴하게
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div className={styles.storehome_shopping_reason_card}>
                            <div className={styles.storehome_shopping_reason_card_container}>
                                <div className={styles.storehome_shopping_reason_card_container_card}>
                                    <div className={styles.storehome_shopping_reason_card_container_icon}>
                                        <svg width="49" height="56" viewBox="0 0 49 56" className={styles.card_icon} aria-hidden="true">
                                            <path d="m0 0h49v56h-49z" fill="none"></path>
                                            <path d="m47.8447 27.501-6.6758-7.1289c-.9111-.9619-1.9541-1.3721-3.4854-1.3721h-4.6836v-4c0-2.7614-2.2385-5-5-5h-22.9999c-2.7615 0-5 2.2386-5 5v21c0 2.7614 2.2385 5 5 5h1.1504c.2532 2.8719 2.6616 5.125 5.5996 5.125s5.3464-2.2531 5.5996-5.125h13.8008c.2532 2.8719 2.6616 5.125 5.5996 5.125s5.3464-2.2531 5.5996-5.125h2.6436c2.5469 0 4.0068-1.4092 4.0068-3.8657v-6.7515c0-1.0835-.4268-2.1396-1.1553-2.8818zm-32.5202 13.499c-.2463 1.7609-1.7468 3.125-3.5745 3.125s-3.3281-1.3641-3.5745-3.125c-.0232-.165-.0505-.3288-.0505-.5 0-.5364.1245-1.0415.3345-1.5.5725-1.2501 1.8281-2.125 3.2905-2.125s2.718.8749 3.2905 2.125c.21.4585.3345.9636.3345 1.5 0 .1712-.0273.335-.0505.5zm15.6755-2h-13.8335c-.6572-2.3773-2.8301-4.125-5.4165-4.125s-4.7593 1.7477-5.4165 4.125h-1.3335c-1.6543 0-3-1.3458-3-3v-21c0-1.6542 1.3457-3 3-3h23c1.6543 0 3 1.3458 3 3zm9.3245 2c-.2463 1.7609-1.7468 3.125-3.5745 3.125s-3.3281-1.3641-3.5745-3.125c-.0232-.165-.0505-.3288-.0505-.5 0-.5364.1245-1.0415.3345-1.5.5725-1.2501 1.8281-2.125 3.2905-2.125s2.718.8749 3.2905 2.125c.21.4585.3345.9636.3345 1.5 0 .1712-.0273.335-.0505.5zm6.6755-3.8657c0 1.3252-.5811 1.8657-2.0068 1.8657h-2.8267c-.6572-2.3773-2.8301-4.125-5.4165-4.125-1.4429 0-2.7544.5478-3.75 1.4407v-15.3157h4.6836c.9785 0 1.5107.1958 2.0303.7437l6.6875 7.1411c.375.3823.5986.9424.5986 1.498zm-3.3914-8.0216c.2444.2794.3914.493.3914.8873h-7.7773c-.75 0-1.2227-.4766-1.2227-1.2324v-5.7676h2.4131c.5703 0 .9944.23 1.3364.6244z"></path>
                                        </svg>
                                    </div>
                                    <div className={styles.storehome_shopping_reason_card_container_text}>
                                        간편한 무료 배송. 매장 보유 제품은 Apple Store에서 직접 픽업 가능.
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div className={styles.storehome_shopping_reason_card}>
                            <div className={styles.storehome_shopping_reason_card_container}>
                                <div className={styles.storehome_shopping_reason_card_container_card}>
                                    <div className={styles.storehome_shopping_reason_card_container_icon}>
                                        <svg width="40" height="56" viewBox="0 0 40 56" className={styles.card_icon_elevated_purple} aria-hidden="true">
                                            <path d="m0 0h40v56h-40z" fill="none"></path>
                                            <path d="m32.7812 29.6094a1.0221 1.0221 0 0 0 -1-.125 42.9866 42.9866 0 0 1 -5.76 1.3437 37.7 37.7 0 0 1 -6.01.4688 37.8947 37.8947 0 0 1 -6.0208-.4688 42.1134 42.1134 0 0 1 -5.75-1.3437 1.08 1.08 0 0 0 -1.0313.125.9492.9492 0 0 0 -.2812.9583 12.0862 12.0862 0 0 0 2.1875 5.6667 13.3019 13.3019 0 0 0 4.6446 4.0521 13.0763 13.0763 0 0 0 6.25 1.51 13.0332 13.0332 0 0 0 6.2292-1.51 13.3984 13.3984 0 0 0 4.6562-4.0521 11.8567 11.8567 0 0 0 2.1771-5.6667.9968.9968 0 0 0 -.2913-.9583zm-2.3124 4.4167a37.2669 37.2669 0 0 1 -5.1771 1.0939 38.5047 38.5047 0 0 1 -5.2813.3646 38.8064 38.8064 0 0 1 -5.2812-.3646 37.13 37.13 0 0 1 -5.198-1.0937 9.7 9.7 0 0 1 -1.0833-2.9167 43.2962 43.2962 0 0 0 5.6459 1.2292 39.8385 39.8385 0 0 0 5.9166.4375 39.9092 39.9092 0 0 0 5.9063-.4375 42.4138 42.4138 0 0 0 5.6354-1.2292 9.43 9.43 0 0 1 -1.0833 2.9165zm-17.8021-8.5834a2.8583 2.8583 0 0 1 0-3.5416 1.8441 1.8441 0 0 1 1.4271-.7084 1.9442 1.9442 0 0 1 1.4895.7084 2.7531 2.7531 0 0 1 -.01 3.5312 1.944 1.944 0 0 1 -1.4791.7188 1.8438 1.8438 0 0 1 -1.4275-.7084zm11.7812-.01a2.8064 2.8064 0 0 1 0-3.5312 1.8745 1.8745 0 0 1 1.4375-.7084 1.8935 1.8935 0 0 1 1.4583.7084 2.8207 2.8207 0 0 1 0 3.5416 1.8931 1.8931 0 0 1 -1.4583.7084 1.8644 1.8644 0 0 1 -1.4375-.7192zm-4.4479-14.7327a17.3 17.3 0 1 1 -17.3 17.3 17.32 17.32 0 0 1 17.3-17.3m0-2.2a19.5 19.5 0 1 0 19.5 19.5 19.5 19.5 0 0 0 -19.5-19.5z"></path>
                                        </svg>
                                    </div>
                                    <div className={styles.storehome_shopping_reason_card_container_text}>
                                        자신만의 것이라는 증표.<br/> 무료로 조합해서 새기는 <br/>이모티콘, 이름, 숫자.
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div className={styles.storehome_shopping_reason_card}>
                            <div className={styles.storehome_shopping_reason_card_container}>
                                <div className={styles.storehome_shopping_reason_card_container_card}>
                                    <div className={styles.storehome_shopping_reason_card_container_icon}>
                                        <svg viewBox="0 0 36 56" width="36" height="56" className={styles.card_icon_elevated_navy} aria-hidden="true">
                                            <path fill="none" d="M0 0H36V56H0z"></path>
                                            <path d="M29 10H7a7 7 0 0 0-7 7v22a7 7 0 0 0 7 7h22a7 7 0 0 0 7-7V17a7 7 0 0 0-7-7zm5 29c0 2.757-2.243 5-5 5H7c-2.757 0-5-2.243-5-5V17c0-2.757 2.243-5 5-5h22c2.757 0 5 2.243 5 5v22zm-9-20h-2.038c-.195-2.46-2.329-4.405-4.962-4.405S13.233 16.54 13.038 19H11a3.5 3.5 0 0 0-3.5 3.5v13A3.5 3.5 0 0 0 11 39h14a3.5 3.5 0 0 0 3.5-3.5v-13A3.5 3.5 0 0 0 25 19zm-3.458 11.447a5.733 5.733 0 0 1-.475.873c-.246.364-.45.618-.61.754-.237.229-.5.347-.78.356-.194 0-.44-.06-.72-.178a2.019 2.019 0 0 0-.779-.178c-.246 0-.508.06-.796.178-.288.119-.517.178-.695.186-.263.009-.525-.11-.797-.364-.169-.152-.38-.407-.635-.78a5.597 5.597 0 0 1-.67-1.372 5.184 5.184 0 0 1-.279-1.635c0-.602.127-1.119.382-1.56.194-.347.465-.626.796-.83a2.151 2.151 0 0 1 1.084-.313c.212 0 .492.06.839.195.339.136.56.203.66.203.077 0 .323-.076.738-.237.39-.144.729-.203 1-.178.737.06 1.287.356 1.66.898-.66.415-.991.992-.982 1.729.008.576.211 1.058.601 1.432.186.177.39.313.61.406-.042.144-.102.28-.152.415zm-3.56-5.151c0-.44.162-.847.493-1.228.169-.196.372-.348.627-.475.245-.127.483-.203.711-.212.009.06.009.119.009.178 0 .45-.161.881-.483 1.271-.39.466-.839.678-1.348.635-.008-.05-.008-.11-.008-.17zM14.24 19c.194-1.794 1.796-3.205 3.761-3.205s3.567 1.41 3.761 3.205H14.24z"></path>
                                        </svg>
                                    </div>
                                    <div className={styles.storehome_shopping_reason_card_container_text}>
                                        맞춤형 쇼핑을 Apple Store앱에서 경험하세요.
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div className={styles.storehome_shopping_reason_card}>
                            <div className={styles.storehome_shopping_reason_card_container}>
                                <div className={styles.storehome_shopping_reason_card_container_card}>
                                    <div className={styles.storehome_shopping_reason_card_container_icon}>
                                        <svg viewBox="0 0 36 56" width="36" height="56" className={styles.card_icon_elevated_navy} aria-hidden="true">
                                            <path fill="none" d="M0 0H36V56H0z"></path>
                                            <path id="path2324" d="m 14.9,14.43 a 2.581,2.581 0 0 1 -0.472,-0.045 3.083,3.083 0 0 1 -0.067,-0.629 7.531,7.531 0 0 1 1.909,-4.694 7.76,7.76 0 0 1 5.1,-2.628 3.329,3.329 0 0 1 0.067,0.7 7.745,7.745 0 0 1 -1.837,4.825 6.728,6.728 0 0 1 -4.7,2.471 z m 12.807,3.818 a 7.851,7.851 0 0 0 -3.751,6.6 7.64,7.64 0 0 0 4.649,7.008 18.257,18.257 0 0 1 -2.381,4.919 c -1.482,2.134 -3.032,4.268 -5.391,4.268 -2.359,0 -2.965,-1.37 -5.683,-1.37 -2.65,0 -3.594,1.415 -5.75,1.415 -2.156,0 -3.661,-1.977 -5.391,-4.4 A 21.279,21.279 0 0 1 0.395,25.211 c 0,-6.738 4.38,-10.31 8.692,-10.31 2.291,0 4.2,1.5 5.638,1.5 1.37,0 3.5,-1.595 6.109,-1.595 a 8.172,8.172 0 0 1 6.873,3.442 z"></path>
                                        </svg>
                                    </div>
                                    <div className={styles.storehome_shopping_reason_card_container_text}>
                                        Mac을 맞춤 구성하고,<br/> Apple Watch를 당신만의 스타일로.
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>

                {/* 액세서리 카드 */}
                <div className={styles.storehome_shopping_product_accessories}>
                    <div className={styles.storehome_shopping_product_accessories_container}>
                        <div className={styles.storehome_shopping_product_accessories_header}>
                            <span className={styles.storehome_title_text_black}>액세서리.</span>
                            <span className={styles.storehome_title_text_gray}>즐겨 사용하는 기기들과 완벽하게 페어링되는 여러 가지 필수품.</span>
                        </div>
                        <div className={styles.storehome_shopping_product_accessories_main}>
                            <div className={styles.storehome_shopping_product_accessories_main_card_container}>
                                <Card400 name="새로움을 입다." describe="사랑받는 액세서리들로 더욱 신선하고 다채롭게" describeType="black" path="#" image="https://store.storeimages.cdn-apple.com/1/as-images.apple.com/is/store-card-40-accessories-story-202503?wid=800&hei=1000&fmt=p-jpg&qlt=95&.v=K1NBYnFSRndoRHEyUklJLyttMlQ2TDJZSWVLNGdhSUJlSmNGa21DNVh4dEM0NE1nb1loei9zeXJYUS9EcFBOenN2Mmx4a3VvSnUzaFUvSVlVRUJkbEFxYi9OZSszSzhrMXYreWkvWm03emFWZjFod0MwSDdqOFJDWWdyWjF0NmQ"/>
                            </div>
                            <div className={styles.storehome_shopping_product_accessories_main_card_container_card}>
                                <Card313 category="MagSafe형 iPhone 16 Pro Max 실리콘 케이스 - 피오니"/>
                            </div>
                            <div className={styles.storehome_shopping_product_accessories_main_card_container_card}>
                                <Card313 category="Tech21 FlexQuartz (iPhone 16 Pro Max) (MagSafe 호환) - 스누피"/>
                            </div>
                            <div className={styles.storehome_shopping_product_accessories_main_card_container_card}>
                                <Card313 category="Tech21 EvoArt Snoopy Case for AirPods Pro 2 - 체리 블라섬"/>
                            </div>
                            <div className={styles.storehome_shopping_product_accessories_main_card_container_card}>
                                <Card313 category="Tech21 EvoArt Sboopy Case(AirPods Max) - 체리 블라섬"/>
                            </div>
                            <div className={styles.storehome_shopping_product_accessories_main_card_container_card}>
                                <Card313 category="Herschel Heritage Shoulder Bag - 스누피 체리 블라섬 핑크"/>
                            </div>
                            <div className={styles.storehome_shopping_product_accessories_main_card_container_card}>
                                <Card313 category="Herschel Settlement Hip Pack - 스누피 체리 블라섬 핑크"/>
                            </div>
                            <div className={styles.storehome_shopping_product_accessories_main_card_container_card}>
                                <Card313 category="PoPSocket Magsafe Grip (iPhone) - 찰리 브라운 체리 블라섬"/>
                            </div>
                            <div className={styles.storehome_shopping_product_accessories_main_card_container_card}>
                                <Card313 category="Nimble Champ 10k Portable Charger - 스누피 체리 블라섬 화이트"/>
                            </div>
                            <div className={styles.storehome_shopping_product_accessories_main_card_container_card}>
                                <Card313 category="MagSafe형 iPhone 16 투명 케이스"/>
                            </div>
                            <div className={styles.storehome_shopping_product_accessories_main_card_container_card}>
                                <Card313 category="46mm 프라이드 에디션 스포츠 밴드 - M/L"/>
                            </div>
                            <div className={styles.storehome_shopping_product_accessories_main_card_container}>
                                <Card400 name="모든 액세서리를 살펴보세요."  path="#" image="https://store.storeimages.cdn-apple.com/1/as-images.apple.com/is/store-card-40-accessories-explore-202503?wid=800&hei=1000&fmt=p-jpg&qlt=95&.v=K1NBYnFSRndoRHEyUklJLyttMlQ2SnBtVU93bDBEbzYrK1JUSkZGdW9DL2MwYUZxUnpyb2ZTRDZWVnQ1cEF1MVVrc1JZVkQ0S2s0elFpK2Y1K2lCS1NsOG1PN3FBRzN3cEphZ2ZrZllTNFpGYkNtaGFzRk0vZUhKUytGb2tsRU0"/>
                            </div>
                        </div>
                    </div>
                </div>

                {/*음향기기 쇼핑 카드 */}
                <div className={styles.storehome_shopping_product_audio}>
                    <div className={styles.storehome_shopping_product_audio_container}>
                        <div className={styles.storehome_shopping_product_audio_header }>
                            <span className={styles.storehome_title_text_black}>음향기기.</span>
                            <span className={styles.storehome_title_text_gray}>즐겨 사용하는 기기들과 완벽하게 페어링되는 여러 가지 필수품.</span>
                        </div>
                        <div className={styles.storehome_shopping_product_audio_main}>
                            <div className={styles.storehome_shopping_product_audio_main_card_container}>
                                <Card400 name="Apple Music 3개월 무료 이용 혜택." describe="해당 Apple 기기 구입 시 혜택 제공." describeType="black" path="#" image="https://store.storeimages.cdn-apple.com/1/as-images.apple.com/is/store-card-50-apple-music-202412?wid=800&hei=1000&fmt=p-jpg&qlt=95&.v=SFNxMjRYSTFLdjBJZG1UYjBKRUNDc21KWElzeGUrOVROazhWUi9vMy9xUnFTRjNxbmh1UnU2R29ibGdpZUFXc0prY3crUWRsN1dqVjRnMHR5S1hVbkVOdXo5Z2c3b1kwaDdELytwanYzTEc2S2VFaVNLbFRwRnRocGdXWjBnQ0Y"/>
                            </div>
                            <div className={styles.storehome_shopping_product_audio_main_card_container_card}>
                                <Card313 category="AirPods 4 액티브 노이즈 캔슬링 모델"/>
                            </div>
                            <div className={styles.storehome_shopping_product_audio_main_card_container_card}>
                                <Card313 category="Airpod pro 2"/>
                            </div>
                            <div className={styles.storehome_shopping_product_audio_main_card_container_card}>
                                <Card313 category="Powerbeats Pro2 - 고성능 이어버드 - 일렉트릭 오렌지"/>
                            </div>
                            <div className={styles.storehome_shopping_product_audio_main_card_container_card}>
                                <Card313 category="AirPods Max - 미드나이트"/>
                            </div>
                            <div className={styles.storehome_shopping_product_audio_main_card_container_card}>
                                <Card313 category="Beats Solo 4 - 온이어 Wireless헤드폰 - 클라우드 핑크"/>
                            </div>
                            <div className={styles.storehome_shopping_product_audio_main_card_container_card}>
                                <Card313 category="Beats Pill - 무선 Bluetooth 블루투스 스피커 - 샴페인 골드"/>
                            </div>
                        </div>
                    </div>
                </div>
                {/* 서비스 카드 */}
                <div className={styles.storehome_shopping_service}>
                    <div className={styles.storehome_shopping_service_container}>
                        <div className={styles.storehome_shopping_service_container_header}>
                            <span className={styles.storehome_title_text_black}>Apple 경험.</span>
                            <span className={styles.storehome_title_text_gray}>Apple 제품 및 서비스로 더욱더 많은 걸 누리다.</span>
                        </div>
                        <div className={styles.storehome_shopping_service_container_main}>
                            <div className={styles.storehome_shopping_service_container_main_card_container}>
                                <Card480  text="손쉬운 사용" name="손쉬운 사용을 염두에 둔 혁신." cardType="small" path="#" image="https://store.storeimages.cdn-apple.com/1/as-images.apple.com/is/store-card-50-apple-experience-202505?wid=960&hei=1000&fmt=p-jpg&qlt=95&.v=SFNxMjRYSTFLdjBJZG1UYjBKRUNDdXZWOStqTk4vWFIzdExWRHpGMjVKQVVZcUZCTytmVGYydzVnTU9GdnZsaW1td3JHMmlHM0d0VzBMMGs5ZHR4WjhoejZkczZLT2pDNXRIRCtIQjF1RFFidXZEK1ByV3pwM2hLc3BWdTJxQUU"/>
                            </div>
                            <div className={styles.storehome_shopping_service_container_main_card_container}>
                                <Card480  name="Apple Intelligence. 글을 쓰고, 개성을 표출하고, 이것저것 척척"  path="#" image="https://store.storeimages.cdn-apple.com/1/as-images.apple.com/is/store-card-50-apple-intelligence-202503_GEO_KR?wid=960&hei=1000&fmt=p-jpg&qlt=95&.v=SFNxMjRYSTFLdjBJZG1UYjBKRUNDalZCM0g0MTRQL0NONjZoQUpUNEpyYnhVMDMrUnVWYnFtallyQ1hyYmZpMENJWGJVR3BNa0NheTNxZUJ3blJNRk1mSGN3NTUxbDRHZDZXK1V3b1o4a1RHM1FEZytkNUFtWmRjeWJiaTlKb3Rka0xmckVNVTBkS20yTzkwa0dhU09n"/>
                            </div>
                            <div className={styles.storehome_shopping_service_container_main_card_container}>
                                <Card480  text="Apple Store  앱" name="선물이 곧 도착한다는 걸 미리 알려주세요" describe="보내는 이도 받는 이도 기분 좋아지는 디지털 메시지. 선물과 함께 원하는 날짜에 전해보세요." path="#" image="https://store.storeimages.cdn-apple.com/1/as-images.apple.com/is/store-card-50-mothers-day-gifting-202504?wid=960&hei=1000&fmt=p-jpg&qlt=95&.v=ODZqNTg1VE5NZ3RHb1Y5anVuNWU0LytmcDNHN2dUdHNNTjJaTnEycnV2WFJjSU5pUVVGNEFDMTFiYjdEOUFsSVVrc1JZVkQ0S2s0elFpK2Y1K2lCS1NsOG1PN3FBRzN3cEphZ2ZrZllTNFpBaVR3VWVpRHAvdjJOb2ozaDYzVUc"/>
                            </div>
                            <div className={styles.storehome_shopping_service_container_main_card_container}>
                                <Card480  text="Apple TV+" name="Apple 기기를 구입하면 Apple TV+가 3개월 무료.*"  path="#" image="https://store.storeimages.cdn-apple.com/1/as-images.apple.com/is/store-card-50-tv-services-202501_GEO_KR?wid=960&hei=1000&fmt=p-jpg&qlt=95&.v=R0NBWk45ZjFvOUNHNjZCZ0VmMkVtQmxxSkhNcjROaFBiMC9VNFhXbTZEbnBST0JBMmIvNmxqRzk3VEM5Uy9jSnU2S1NDY0Mybzd2UUxDKzhkSmN0dERrMTFvNEM2eG1yOHVjc2VHR05XMERYZ3A0aHhkSFdXYkN2dUtzWmF0QW4"/>
                            </div>
                            <div className={styles.storehome_shopping_service_container_main_card_container}>
                                <Card480  name="네 가지 Apple 서비스. 한 번의 간편한 가입." cardType="small" path="#" image="https://store.storeimages.cdn-apple.com/1/as-images.apple.com/is/store-card-50-subscriptions-202108?wid=960&hei=1000&fmt=p-jpg&qlt=95&.v=WW05TjdlcC83b2p3NDlrR3ZVbk1xYmJOQmJzSVJ3UFJiNTcwZlp0V0h2dlNTMm5RTnVQcDVKVGwvVHBJTkp3VFN5aWNYUFpIbkFhdm03T3BzSjdVSThtd3k4VkkwQ2l3cXZ6cEkycldOaXl2REFGU3hIOFJyRWo1cXgzVWNKbGY"/>
                            </div>
                            <div className={styles.storehome_shopping_service_container_main_card_container}>
                                <Card480  name="보다 오래 안심할 수 있도록." describe="이제 AppleCare+가 우발적인 손상에 대한 수리 서비스를 횟수 제한 없이 제공합니다." cardType="small" path="#" image="https://store.storeimages.cdn-apple.com/1/as-images.apple.com/is/store-card-50-applecare-202503?wid=960&hei=1000&fmt=p-jpg&qlt=95&.v=SFNxMjRYSTFLdjBJZG1UYjBKRUNDaXRXOGV1M2ZHcDVxZzhMK2cxK3dsTUloZHRRYWt5UUpyTGVwNEhDZEV3VXg4ZHpEbm5XWGdaM3BiNVRDaG55Ukc2ZjdMSUNqeUNFYjF1MU1sS2U0a3E1dDgvV3BhU1hoSzFPUEZjam5HQ2g"/>
                            </div>
                            <div className={styles.storehome_shopping_service_container_main_card_container}>
                                <Card480  text="" name="Apple Pay 사용법을 모두 알아보세요." cardType="small"  path="#" image="https://store.storeimages.cdn-apple.com/1/as-images.apple.com/is/store-card-50-applepay-202503?wid=960&hei=1000&fmt=p-jpg&qlt=95&.v=SFNxMjRYSTFLdjBJZG1UYjBKRUNDdUVMeDhuVU80VmJvRWgxZU1CTTZlMmo2Z1ptREdBenZRTjZuSCtBemFnUTRHeXB5TnVsU3R6Qjd0Y2JzbURyWERKTGY0SktEdXAyaG9IZWxWT3NMZzErYWpGdS9XeFgvbS9ITnNYOEhYaG4"/>
                            </div>
                            <div className={styles.storehome_shopping_service_container_main_card_container}>
                                <Card480  text="홈" name="앱 하나로 집안 전체를 관리하는 방법을 알아보세요." cardType="small"  path="#" image="https://store.storeimages.cdn-apple.com/1/as-images.apple.com/is/store-card-50-homekit-202405_GEO_KR?wid=960&hei=1000&fmt=p-jpg&qlt=95&.v=UWdrNzNrY0ZiOGhRNlVuUlF4U3JoejVHYVpyWFdSYy85NGlTbU1VNHZsOFBydHo5aldMOTRYbjRSM1lCK1Nra2Nva0xZQWFEV2ljOWRGNWZJRk4vWGgvOERJNEJMdXB2K2JwM2I2YmhadytMQW1saTRVVjVlUW5QdVdlb0dJUWQ"/>
                            </div>
                        </div>
                    </div>
                </div>
                {/*  혜택 카드 */}
                <div className={styles.storehome_shopping_benefit}>
                    <div className={styles.storehome_shopping_benefit_container}>
                        <div className={styles.storehome_shopping_benefit_container_header}>
                            <span className={styles.storehome_title_text_black}>특별 할인.</span>
                            <span className={styles.storehome_title_text_gray}>비즈니스,학교 등을 위한 혜택.</span>
                        </div>
                        <div className={styles.storehome_shopping_benefit_container_main}>
                            <div className={styles.storehome_shopping_benefit_container_main_card}>
                                <Card400 text="교육" name="새로운 Mac 또는 iPad를 교육 할인가로 더욱 부담 없이."  path="#" image="https://store.storeimages.cdn-apple.com/1/as-images.apple.com/is/store-card-40-bts-edu-macbook-air-ipad-air-202503?wid=800&hei=1000&fmt=p-jpg&qlt=95&.v=bTAvUVhobndWL01MVC9aenBVVGo5YWZmUzB4a3czWENOTU1QWVJ1K01WWk5LOEsyMEhpRHE1T1EzSDFwQVpKVzF1WTFUcUFiTi80Y2ZLM2ZEQmtMcjJhUXpzSGp3b1lnNUp6M2lSQzZEVVBiYmVpOUU2RG04OHJUUjJybTZTeHFHaXB3VUEzd1huUnhZRnQ3eTQ1QUdB"/>
                            </div>
                            <div className={styles.storehome_shopping_benefit_container_main_card}>
                                <Card400 text="인증 리퍼비쉬 제품" name="1년 보증이 제공되는 리퍼비쉬 Apple 제품을 쇼핑하세요"  path="#" image="https://store.storeimages.cdn-apple.com/1/as-images.apple.com/is/store-card-40-refurb-202408_GEO_KR?wid=800&hei=1000&fmt=p-jpg&qlt=95&.v=MTZ5STlsTFBndFBGTjdlaHEreGY1WVpjRk5RUmNDUnRpcEtwZE90QWhHTVd5Vmc3Z0FwOExzY2czeWpSSWVybFN5aWNYUFpIbkFhdm03T3BzSjdVSTg3eG9qTElWODhsN0VFL2hKVnFlRXFSQzlQOERDWGFFVzNYcmJ6Wlc5V2k"/>
                            </div>
                            <div className={styles.storehome_shopping_benefit_container_main_card}>
                                <Card400 text="비즈니스" name="대기업부터 중소기업까지 Apple이 함께합니다." nameType="white"  path="#" image="https://store.storeimages.cdn-apple.com/1/as-images.apple.com/is/iphone-card-40-business-202409_GEO_KR?wid=800&hei=1000&fmt=jpeg&qlt=90&.v=alV4a1Q5dWpXakxENUdPdUc5bk5oL3AvbkFpTUJaVTl5YXRNYno3eGE5Zy8yNUxISW1HalFpaHFsZFpmVHh5STczTGJ1bkVZOVdxMC9CSUwydmQ4a0hWWkNsdDY3bTJMWkdROWF0V1BxMU5yVGw0bkxzSmlGWFlVcG00Qzg0MG0"/>
                            </div>
                        </div>
                    </div>
                </div>

                {/* 빠른 링크*/}
                <div className={styles.storehome_shopping_quick_link}>
                    <div className={styles.storehome_shopping_quick_link_header}>
                        <span className={styles.storehome_title_text_black}>빠른 링크.</span>
                    </div>
                    <div className={styles.storehome_shopping_quick_link_main}>
                        <ul>
                            <li>
                                <a className={styles.storehome_shopping_quick_link_main_button}>
                                    <Button text="매장 찾기" type="black" path="#" />
                                </a>
                            </li>
                            <li>
                                <a className={styles.storehome_shopping_quick_link_main_button}>
                                    <Button text="주문 상태" type="black" path="#" />
                                </a>
                            </li>
                            <li>
                                <a className={styles.storehome_shopping_quick_link_main_button}>
                                    <Button text="쇼핑 도움말" type="black" path="#" />
                                </a>
                            </li>
                            <li>
                                <a className={styles.storehome_shopping_quick_link_main_button}>
                                    <Button text="반품" type="black" path="#" />
                                </a>
                            </li>
                            <li>
                                <a className={styles.storehome_shopping_quick_link_main_button}>
                                    <Button text="관심 목록" type="black" path="#" />
                                </a>
                            </li>
                        </ul>
                    </div>

                </div>
            </main>
        </>
    );
};

export default StoreHome;