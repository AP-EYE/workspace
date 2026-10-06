import com.google.i18n.phonenumbers.*;
import java.util.regex.*;
public class Probe {
public static boolean isPhoneNumber(String mobileNumber) {
        boolean lengthCondition = mobileNumber.length() < 8 || mobileNumber.length() > 16;
        if (lengthCondition) return false;
        boolean alphabetsCondition = mobileNumber.toLowerCase() != mobileNumber.toUpperCase(); // contains alphabets

        if (alphabetsCondition) return false;

        PhoneNumberUtil phoneNumberUtil = PhoneNumberUtil.getInstance();

        // isPossibleNumber computes faster than parse but less accuracy
        boolean check = phoneNumberUtil.isPossibleNumber(mobileNumber,
                    Phonenumber.PhoneNumber.CountryCodeSource.UNSPECIFIED.name());
        if (!check) {
            return false;
        }

        try {
            Phonenumber.PhoneNumber phone = phoneNumberUtil.parse(mobileNumber,
                    Phonenumber.PhoneNumber.CountryCodeSource.UNSPECIFIED.name());
            return phoneNumberUtil.isValidNumber(phone);
        } catch (Exception e) {
            // eat it
            return false;
        }

    }
public static void main(String[] args) {
PhoneNumberUtil u=PhoneNumberUtil.getInstance();
for(String region:new String[]{"US","GB","FR","DE","FI","IN","JP","CA","KR"}) {
var p=u.getExampleNumberForType(region,PhoneNumberUtil.PhoneNumberType.MOBILE);
for(var f: new PhoneNumberUtil.PhoneNumberFormat[]{PhoneNumberUtil.PhoneNumberFormat.E164,PhoneNumberUtil.PhoneNumberFormat.NATIONAL,PhoneNumberUtil.PhoneNumberFormat.INTERNATIONAL}) {
String s=u.format(p,f); System.out.println("PHONE\t"+region+"\t"+f+"\t"+isPhoneNumber(s)+"\t"+s);
}
String s=u.format(p,PhoneNumberUtil.PhoneNumberFormat.NATIONAL).replaceAll("[^0-9]","");
System.out.println("PHONE\t"+region+"\tDIGITS\t"+isPhoneNumber(s)+"\t"+s);
}
System.out.println("REGEX\t0\t"+Pattern.compile("[A-Z]{5}[0-9]{4}[A-Z]{1}").matcher("ABCDE1234F").matches());
System.out.println("REGEX\t1\t"+Pattern.compile("[A-Z]{5}[0-9]{4}[A-Z]{1}").matcher("PAN: ABCDE1234F").matches());
System.out.println("REGEX\t2\t"+Pattern.compile("[0-9]{9}[A-Za-z]{1}[0-9a-zA-Z]?").matcher("123456789A").matches());
System.out.println("REGEX\t3\t"+Pattern.compile("[0-9]{9}[A-Za-z]{1}[0-9a-zA-Z]?").matcher("1EG4TE5MK73").matches());
System.out.println("REGEX\t4\t"+Pattern.compile("[0-9]{14}").matcher("00000000000000").matches());
System.out.println("REGEX\t5\t"+Pattern.compile("(?!BG)(?!GB)(?!NK)(?!KN)(?!NT)(?!TN)(?!ZZ)(?! ?.O)[A-CE-EG-HJ-PR-TW-Za-ce-eg-hj-pr-tw-z]{2}[0-9]{6}[A-Da-d]{1}").matcher("QQ123456C").matches());
System.out.println("REGEX\t6\t"+Pattern.compile("(?!BG)(?!GB)(?!NK)(?!KN)(?!NT)(?!TN)(?!ZZ)(?! ?.O)[A-CE-EG-HJ-PR-TW-Za-ce-eg-hj-pr-tw-z]{2}[0-9]{6}[A-Da-d]{1}").matcher("AB123456C").matches());
System.out.println("REGEX\t7\t"+Pattern.compile("(?!BG)(?!GB)(?!NK)(?!KN)(?!NT)(?!TN)(?!ZZ)(?! ?.O)[A-CE-EG-HJ-PR-TW-Za-ce-eg-hj-pr-tw-z]{2}[0-9]{6}[A-Da-d]{1}").matcher("AB 12 34 56 C").matches());
System.out.println("REGEX\t8\t"+Pattern.compile("([0-2][0-9]|[3-3][0-1])([0-0][1-9]|[1-1][0-2])[0-9]{2}[Aa\\+\\-]{1}([0-8][0-9][2-8]|[1-8][0-9][0-9])[0-9A-Ya-y]").matcher("310299-123A").matches());
System.out.println("REGEX\t9\t"+Pattern.compile("([0-2][0-9]|[3-3][0-1])([0-0][1-9]|[1-1][0-2])[0-9]{2}[Aa\\+\\-]{1}([0-8][0-9][2-8]|[1-8][0-9][0-9])[0-9A-Ya-y]").matcher("010101B123A").matches());
System.out.println("REGEX\t10\t"+Pattern.compile("[0-9]{9}").matcher("000000000").matches());
System.out.println("REGEX\t11\t"+Pattern.compile("[0-9]{9}").matcher("123456789").matches());
System.out.println("REGEX\t12\t"+Pattern.compile("[0-9]{9}").matcher("123 456 789").matches());
System.out.println("REGEX\t13\t"+Pattern.compile("[0-9]{2}([0-2][0-9]|[3-3][0-1])([0-0][1-9]|[1-1][0-2])[0-9]{2}[A-Za-z][0-9]{3}").matcher("12310299A123").matches());
System.out.println("REGEX\t14\t"+Pattern.compile("[0-9]{12}").matcher("000000000000").matches());
System.out.println("REGEX\t15\t"+Pattern.compile("[0-9]{12}").matcher("1234-5678-9012").matches());
System.out.println("REGEX\t16\t"+Pattern.compile("[A-Z]{2}?[ ]?[0-9]{2}[ ]?\\s*(\\d{4}\\s*){4,10}(\\d{1,2}\\s*)?").matcher("GB82WEST12345698765432").matches());
System.out.println("REGEX\t17\t"+Pattern.compile("[A-Z]{2}?[ ]?[0-9]{2}[ ]?\\s*(\\d{4}\\s*){4,10}(\\d{1,2}\\s*)?").matcher("DE89370400440532013000").matches());
System.out.println("REGEX\t18\t"+Pattern.compile("[A-Z]{2}?[ ]?[0-9]{2}[ ]?\\s*(\\d{4}\\s*){4,10}(\\d{1,2}\\s*)?").matcher("DE00370400440532013000").matches());
System.out.println("REGEX\t19\t"+Pattern.compile("\\d{1,5}(\\s[\\w-.,]*){1,6},\\s[A-Z]{2}\\s\\d{5}\\b").matcher("123 Example St, CA 90210").matches());
System.out.println("REGEX\t20\t"+Pattern.compile("\\d{1,5}(\\s[\\w-.,]*){1,6},\\s[A-Z]{2}\\s\\d{5}\\b").matcher("서울특별시 종로구 예시로 123").matches());
System.out.println("REGEX\t21\t"+Pattern.compile("^[a-zA-Z0-9_+&*-]+(?:\\.[a-zA-Z0-9_+&*-]+)*@(?:[a-zA-Z0-9-]+\\.)+[a-zA-Z]{2,7}$", Pattern.CASE_INSENSITIVE).matcher("alice@example.com").matches());
System.out.println("REGEX\t22\t"+Pattern.compile("^[a-zA-Z0-9_+&*-]+(?:\\.[a-zA-Z0-9_+&*-]+)*@(?:[a-zA-Z0-9-]+\\.)+[a-zA-Z]{2,7}$", Pattern.CASE_INSENSITIVE).matcher("alice@example.technology").matches());
System.out.println("REGEX\t23\t"+Pattern.compile("^[a-zA-Z0-9_+&*-]+(?:\\.[a-zA-Z0-9_+&*-]+)*@(?:[a-zA-Z0-9-]+\\.)+[a-zA-Z]{2,7}$", Pattern.CASE_INSENSITIVE).matcher("문의: alice@example.com").matches());
System.out.println("REGEX\t24\t"+Pattern.compile("^[a-zA-Z0-9_+&*-]+(?:\\.[a-zA-Z0-9_+&*-]+)*@(?:[a-zA-Z0-9-]+\\.)+[a-zA-Z]{2,7}$", Pattern.CASE_INSENSITIVE).matcher("이름@example.com").matches());
System.out.println("REGEX\t25\t"+Pattern.compile("^\\d{3}-\\d{2}-\\d{4}$", Pattern.CASE_INSENSITIVE).matcher("000-00-0000").matches());
System.out.println("REGEX\t26\t"+Pattern.compile("^\\d{3}-\\d{2}-\\d{4}$", Pattern.CASE_INSENSITIVE).matcher("123456789").matches());
}}